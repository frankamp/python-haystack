#!/usr/bin/make -f

LDFLAGS = -ldl
INCLS = 

EXTRA =

CFLAGS = -O2 -g -Wall $(INCLS) $(EXTRA)
CPPFLAGS = -O2 -g -Wall

pid=

H2XML=h2xml.py
XML2PY=xml2py.py

SRCS := $(wildcard *.c *.cpp) 
OBJS := $(patsubst %.c,%,$(SRCS))
OBJS := $(patsubst %.cpp,%,$(OBJS))

DUMPS := $(patsubst %,%.dump,$(OBJS))
OUTLOGS := $(patsubst %,%.stdout,$(OBJS))
PY := $(patsubst test-%,%.py,$(OBJS))

.PHONY: 
	

all: py binaries dumps 

binaries: $(OBJS)

#test-ctypes6: test-ctypes6.cpp
#	$(CC) $(CFLAGS) `pkg-config --cflags QtGui` $<  $(LDFLAGS)  -o $@


%: %.c
	$(CC) $(CFLAGS) $<  $(LDFLAGS)  -o $@
	
%: %.cpp
	$(CXX) $(CPPFLAGS) $<  $(LDFLAGS)  -o $@

%: %.cpp
	$(CXX) `pkg-config --libs --cflags QtGui` $(CPPFLAGS) $<  $(LDFLAGS)  -o $@

py: $(PY)

%.xml: test-%.c
	$(H2XML) -I. $< -o $@

%.xml: test-%.cpp
	$(H2XML) -I. `pkg-config --cflags QtGui` $< -o $@

%.py: %.xml
	$(XML2PY) -kdst $< -o $@


dumps: $(SRCS) $(DUMPS) $(OBJS) 
	
%.dump: %.c 
	sudo python make.py $@
	sudo chown -R jal.jal $@
	
%.dump: %.cpp
	sudo python make.py $@
	sudo chown -R jal.jal $@

	
	
clean: 
	rm -f *~ *.pyc
	rm -f $(OBJS)
	rm -f $(OUTLOGS)
	rm -f $(PY)
	rm -rf $(DUMPS)


