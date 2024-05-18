CC=g++
CFLAGS=-c -Wall -Werror -g -m64 -D_FILE_OFFSET_BITS=64
LDFLAGS = -lfuse -lfuse3

all: main

main: main.o
	$(CC) main.o -o main $(LDFLAGS)
main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

clean:
	rm -rf *o main