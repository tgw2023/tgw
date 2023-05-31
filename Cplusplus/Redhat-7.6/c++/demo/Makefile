CC=gcc
CXX=g++

# 编译器在编译时的参数设置,包含头文件路径设置
CFLAGS:=-Wall -O3 -g
CFLAGS+=-I $(shell pwd)/../include
CXXFLAGS:=-Wall -O3 -g -std=c++11
CXXFLAGS+=-I $(shell pwd)/../include

LIBS_DIR=$(shell pwd)/../lib

# 库文件添加
LDFLAGS:=-lpthread
LDFLAGS+=-Wl,-rpath="$(LIBS_DIR)" -L"$(LIBS_DIR)"
LDFLAGS+=-ltgw
# LDFLAGS+=./lib/libboost_atomic.so.1.62.0
# LDFLAGS+=./lib/libboost_system.so.1.62.0
# LDFLAGS+=./lib/libboost_thread.so.1.62.0
# LDFLAGS+=./lib/libboost_filesystem.so.1.62.0
# LDFLAGS+=./lib/libboost_program_options.so.1.62.0

# 指定源程序存放位置
SRCDIRS:=.

# 设置程序中使用文件类型
SRCEXTS:=.cpp

# 设置运行程序名
PROGRAM:=tgw_demo

SOURCES=$(foreach d,$(SRCDIRS),$(wildcard $(addprefix $(d)/*,$(SRCEXTS))))
OBJS=$(foreach x,$(SRCEXTS),$(patsubst %$(x),%.o,$(filter %$(x),$(SOURCES))))

.PHONY: all clean distclean install

%.o: %.c
	$(CC) -c $(CFLAGS) -o $@ $<
	
%.o: %.cxx
	$(CXX) -c $(CXXFLAGS) -o $@ $<

$(PROGRAM): $(OBJS)
ifeq ($(strip $(SRCEXTS)),.c)
	$(CC) -o $(PROGRAM) $(OBJS) $(LDFLAGS)
else
	$(CXX) -o $(PROGRAM) $(OBJS) $(LDFLAGS)
endif

install:
	install -m 755 -D -p $(PROGRAM) ./bin

clean:
	rm -f $(shell find -name "*.o")
	rm -f $(PROGRAM)
	
distclean:
	rm -f $(shell find -name "*.o")
	rm -f $(shell find -name "*.d")
	rm -f $(PROGRAM)

all:
	@echo $(OBJS)