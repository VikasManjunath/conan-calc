set(CMAKE_CXX_STANDARD 20)
cmake_minimum_required(VERSION 3.20)
project(test VERSION 0.1)

include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
include(CTest)
enable_testing()

add_executable(
  calc_test
  test.cc
)
target_link_libraries(
  calc_test
  gtest_main
  calc
)

include(GoogleTest)
gtest_discover_tests(calc_test)


add_test(hello_test ${EXECUTABLE_OUTPUT_PATH}/calc_test)
add_definitions(-fprofile-arcs -ftest-coverage)
target_link_libraries(calc_test -fprofile-arcs)