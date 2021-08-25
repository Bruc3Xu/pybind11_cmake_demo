# cmake_example for pybind11
python find dynamic library location
1. using rpath in unix/darwin
2. using PATH in windows(os.add_all_directory function when python version >= 3.8)

if you want to set rpath in third-party library, you can use patchelf.
`patchelf --set-rpath '$ORIGIN' lib_a.so`\
$ORIGIN means the library is in same directory with Python lib.

## Prerequisites

**On Unix (Linux, OS X)**

* A compiler with C++11 support
* CMake >= 3.4 or Pip 10+


**On Windows**

* Visual Studio 2015 or newer (required for all Python versions, see notes below)
* CMake >= 3.8 (3.8 was the first version to support VS 2015) or Pip 10+


## Installation

Just clone this repository and pip install. Note the `--recursive` option which is
needed for the pybind11 submodule:

```bash
git clone --recursive https://github.com/pybind/cmake_example.git
cd cmake_example
python setup.py install or pip install .
```

## Test call

```python
import cmake_example
cmake_example.add(1, 2)
```
