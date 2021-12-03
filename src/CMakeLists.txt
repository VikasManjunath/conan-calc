cmake_minimum_required(VERSION 3.1)
set(CMAKE_CXX_FLAGS_PROFILE --coverage)
project(calculator CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(calculator calculator.cpp)
add_definitions(-fprofile-arcs -ftest-coverage)
target_link_libraries(calculator -fprofile-arcs)