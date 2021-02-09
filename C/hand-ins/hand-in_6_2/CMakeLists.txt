cmake_minimum_required(VERSION 3.8)
project(hand_in_6_2)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES main.c student.c student.h print.c)
add_executable(hand_in_6_2 ${SOURCE_FILES} student.c student.h print.c)