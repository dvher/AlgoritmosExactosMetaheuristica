CC=g++
CPPFLAGS=-Wall -Wextra -Wshadow -g -O2
CPPLIBS=
SRCS=$(wildcard *.cpp)

all: build

build: $(SRCS)
	$(CC) $(CPPFLAGS) -o main $(SRCS) $(CPPLIBS)

clean:
	$(RM) main
