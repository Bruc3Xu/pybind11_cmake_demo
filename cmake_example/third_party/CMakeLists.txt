cmake_minimum_required(VERSION 3.4...3.18)
project(a LANGUAGES CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_CURRENT_SOURCE_DIR})
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_CURRENT_SOURCE_DIR})
add_library(a_lib SHARED a.cpp)

add_library(b_lib SHARED b.cpp)
target_link_libraries(b_lib PRIVATE a_lib)