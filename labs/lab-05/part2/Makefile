# Thomas Arturi - CSCI 4470 OSS - Custom Makefile

# Make sure Makefile runs all of the labels
all: static_block dynamic_block

# Static
static_block:
	gcc -c ../source/block.c -o block.o  # Create compiled file
	ar qc static_library.a block.o  # Create static library
	gcc -c ../program.c -o program.o  # Compile program
	gcc program.o static_library.a -o final_static  # Output final with library

# Dynamic
dynamic_block:
	gcc -c ../source/block.c -o block.o  # Create compiled file
	gcc -shared block.o -o dynamic_library.so  # Create dynamic library
	gcc -c ../program.c -o program.o  # Compile program
	gcc -Wl,-rpath=. program.o dynamic_library.so -o final_dynamic  # Output final with library
