cmake_minimum_required(VERSION 3.4...3.18)
project(cmake_example)


include_directories(${CMAKE_SOURCE_DIR}/cmake_example/third_party)

add_subdirectory(pybind11)

add_subdirectory(cmake_example/third_party)


pybind11_add_module(cmake_example src/main.cpp)

# used in exist libraries
# find_library(aa NAMES a_lib b_lib PATH cmake_example/third_party)
# target_link_libraries(cmake_example PRIVATE ${aa})

target_link_libraries(cmake_example PRIVATE a_lib b_lib)
