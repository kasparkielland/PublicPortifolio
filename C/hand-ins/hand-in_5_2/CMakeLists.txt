cmake_minimum_required(VERSION 3.8)
project(hand_in_5_2)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES main.c student.h student.c)
add_executable(hand_in_5_2 ${SOURCE_FILES})