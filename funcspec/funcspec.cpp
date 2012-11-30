#include "llvm/Support/Host.h"
#include "llvm/ADT/IntrusiveRefCntPtr.h"

#include "clang/Frontend/CompilerInstance.h"
#include "clang/Frontend/CompilerInvocation.h"
#include "clang/Basic/TargetOptions.h"
#include "clang/Basic/TargetInfo.h"
#include "clang/Basic/FileManager.h"
#include "clang/Basic/SourceManager.h"
#include "clang/Lex/Preprocessor.h"
#include "clang/Basic/Diagnostic.h"

#include "clang/Lex/HeaderSearch.h"
#include "clang/Frontend/Utils.h"

#include "clang/AST/ASTContext.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/AST/RecursiveASTVisitor.h"
#include "clang/Basic/LangOptions.h"
#include "clang/Parse/Parser.h"
#include "clang/Parse/ParseAST.h"

#include <stdio.h>
#include <iostream>
#include <string>
#include <sstream>
using std::cout;
using std::endl;
using std::string;
using std::cerr;
using std::stringstream;

class MyVisitor : public clang::RecursiveASTVisitor<MyVisitor> {
  public:
    bool VisitFunctionDecl(clang::FunctionDecl *func) {
      clang::DeclarationName name_info = func->getNameInfo().getName();
      string name = name_info.getAsString();
      cout << "  '" << name << "': Spec(" << endl;

      clang::QualType ret_type = func->getResultType();
      string ret_type_str = ret_type.getAsString();
      cout << "    return_type = '" << ret_type_str << "'," << endl;

      cout << "    parameters = [" << endl;
      for (clang::FunctionDecl::param_iterator pi = func->param_begin(), end = func->param_end();
          pi != end; ++pi) {
        clang::QualType param_type = (*pi)->getOriginalType();
        string param_type_str = param_type.getAsString();

        clang::IdentifierInfo* name_id = (*pi)->getIdentifier();

        cout << "      Param(" << endl;
        cout << "        type = '" << param_type_str << "'," << endl;
        cout << "        name = '";
        if (name_id != NULL) {
          cout << name_id->getName().str();
        }
        cout << "'," << endl;
        cout << "      )," << endl;
      }
      cout << "    ]," << endl;

      cout << "  )," << endl;
      return true;
    }

    //bool VisitParmVarDecl(clang::ParmVarDecl *D) {
    //  cout << "YES" << endl;
    //  cout << D->getOriginalType().getAsString() << endl;
    //  return true;
    //}
};

class MyASTConsumer : public clang::ASTConsumer {
  public:
    virtual bool HandleTopLevelDecl( clang::DeclGroupRef d) {
      MyVisitor rv;
      for (clang::DeclGroupRef::iterator it = d.begin(), e = d.end(); it != e; it++) {
        rv.TraverseDecl(*it);
      }
      return true;
    }
};

bool get_cmd_output(string cmd, stringstream &out) {
  FILE* f = popen(cmd.c_str(), "r");
  if (f == 0) {
    cout << "cannot execute:" << cmd << endl;
    return false;
  }
  char buf[4096];
  while (fgets(buf, sizeof(buf), f)) {
    out << string(buf);
  }
  return true;
}

int main(int argc, char* argv[]) {
  if (argc < 3) {
    cout << "usage: " << argv[0] << " <source> <pkg-config libs>..." << endl;
    return 0;
  }

  using clang::CompilerInstance;
  using clang::CompilerInvocation;
  using clang::TargetOptions;
  using clang::TargetInfo;
  using clang::FileEntry;
  using clang::Token;
  using clang::HeaderSearch;
  using clang::HeaderSearchOptions;

  using clang::ASTContext;
  using clang::ASTConsumer;
  using clang::Parser;

  // init compiler
  CompilerInstance ci;
  ci.createDiagnostics(0, NULL);

  llvm::IntrusiveRefCntPtr<TargetOptions> pto( new TargetOptions());
  pto->Triple = llvm::sys::getDefaultTargetTriple();
  TargetInfo *pti = TargetInfo::CreateTargetInfo(ci.getDiagnostics(), pto.getPtr());
  ci.setTarget(pti);

  ci.createFileManager();
  ci.createSourceManager(ci.getFileManager());
  ci.createPreprocessor();
  ci.getPreprocessorOpts().UsePredefines = true;

  MyASTConsumer *astConsumer = new MyASTConsumer();
  ci.setASTConsumer(astConsumer);

  ci.createASTContext();
  ci.createSema(clang::TU_Complete, NULL);

  llvm::IntrusiveRefCntPtr<clang::HeaderSearchOptions> hso( new clang::HeaderSearchOptions());
  HeaderSearch headerSearch(hso,
      ci.getFileManager(),
      ci.getDiagnostics(),
      ci.getLangOpts(),
      pti);

  CompilerInvocation::setLangDefaults(ci.getLangOpts(), clang::IK_C);

  // get gcc include path
  bool ok;
  string gcc_cmd("echo '' | gcc -xc -E -v - 2>&1");
  stringstream gcc_output;
  ok = get_cmd_output(gcc_cmd, gcc_output);
  if (!ok) return -1;
  char line[4096];
  char start_str[] = "#include <...>";
  bool path_started(false);
  while (gcc_output.getline(line, sizeof(line))) {
    if (strncmp(line, start_str, strlen(start_str)) == 0) {
      path_started = true;
    } else if (path_started) {
      if (line[0] == ' ') {
        hso->AddPath(string(line).substr(1), clang::frontend::Angled, false, false, false);
      } else break;
    }
  }

  // get pkg-config include path
  stringstream cmd;
  cmd << "pkg-config --cflags-only-I";
  for (int i = 2; i < argc; i++) {
    cmd << " " << argv[i];
  }
  stringstream output;
  ok = get_cmd_output(cmd.str(), output);
  if (!ok) return -1;
  string include_path;
  while (output >> include_path) {
    hso->AddPath(include_path.substr(2), clang::frontend::Angled, false, false, false);
  }

  clang::InitializePreprocessor(ci.getPreprocessor(), 
      ci.getPreprocessorOpts(),
      *hso,
      ci.getFrontendOpts());

  const FileEntry* pFile = ci.getFileManager().getFile(argv[1]);
  ci.getSourceManager().createMainFileID(pFile);
  ci.getPreprocessor().EnterMainSourceFile();
  ci.getDiagnosticClient().BeginSourceFile(ci.getLangOpts(), &ci.getPreprocessor());

  cout << "\
from collections import namedtuple\n\
Spec = namedtuple('Spec', ['return_type', 'parameters'])\n\
Param = namedtuple('Param', ['name', 'type'])\n\
";
  cout << "func_specs = {" << endl;
  clang::ParseAST(ci.getPreprocessor(), astConsumer, ci.getASTContext());
  cout << "}";

  ci.getDiagnosticClient().EndSourceFile();
  //ci.getASTContext().Idents.PrintStats();
  return 0;
}
