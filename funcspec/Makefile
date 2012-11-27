CXX := clang++
RTTIFLAG := -fno-rtti
LLVMCONFIG := llvm-config

CXXFLAGS := $(shell $(LLVMCONFIG) --cxxflags) $(RTTIFLAG) --std=c++11
LLVMLDFLAGS := $(shell $(LLVMCONFIG) --ldflags --libs $(LLVMCOMPONENTS))

SOURCES = funcspec.cpp

OBJECTS = $(SOURCES:.cpp=.o)
EXES = $(OBJECTS:.o=)
	CLANGLIBS = \
							-lclangTooling\
							-lclangFrontendTool\
							-lclangFrontend\
							-lclangDriver\
							-lclangSerialization\
							-lclangCodeGen\
							-lclangParse\
							-lclangSema\
							-lclangStaticAnalyzerFrontend\
							-lclangStaticAnalyzerCheckers\
							-lclangStaticAnalyzerCore\
							-lclangAnalysis\
							-lclangARCMigrate\
							-lclangRewriteFrontend\
							-lclangRewriteCore\
							-lclangEdit\
							-lclangAST\
							-lclangLex\
							-lclangBasic\
							$(shell llvm-config --libs)

all: $(OBJECTS) $(EXES)

%: %.o
	$(CXX) -o $@ $< $(CLANGLIBS) $(LLVMLDFLAGS)

clean:
	-rm -f $(EXES) $(OBJECTS) *~
