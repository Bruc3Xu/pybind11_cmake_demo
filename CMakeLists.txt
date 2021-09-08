cmake_minimum_required(VERSION 3.4...3.18)
project(cmake_example)


include_directories(${CMAKE_SOURCE_DIR}/cpp/include)

add_subdirectory(pybind11)

add_subdirectory(cpp)


pybind11_add_module(cmake_example src/main.cpp)


find_library(b NAMES libb_lib.so HINTS ${CMAKE_SOURCE_DIR}/cpp/libs)
target_link_libraries(cmake_example PRIVATE ${b})

target_link_libraries(cmake_example PRIVATE a_lib)
