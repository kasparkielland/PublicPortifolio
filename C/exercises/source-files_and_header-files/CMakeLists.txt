cmake_minimum_required(VERSION 3.8)
project(source_files_and_header_files)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES main.c student.c student.h)
add_executable(source_files_and_header_files ${SOURCE_FILES})