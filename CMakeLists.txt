set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_FLAGS_PROFILE --coverage)
cmake_minimum_required(VERSION 3.20)
project(calculator VERSION 0.1)

add_library(calc src/calculator.cpp)
include_directories(src)
add_subdirectory(test)
enable_testing()
