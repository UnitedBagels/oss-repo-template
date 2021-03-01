cmake_minimum_required(VERSION 3.10)
project(program_static)
ADD_LIBRARY( static_block STATIC
             source/block.c )
ADD_EXECUTABLE( program_static
                program.c ) 
TARGET_LINK_LIBRARIES( program_static
                       static_block )

project(program_dynamic)
ADD_LIBRARY( dynamic_block SHARED
             source/block.c )
ADD_EXECUTABLE( program_dynamic
                program.c ) 
TARGET_LINK_LIBRARIES( program_dynamic
                       dynamic_block )