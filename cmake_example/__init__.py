import os
import sys

assert sys.version_info[0] == 3, "only support python3"

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'third_party')
if sys.platform == "win32":
    if sys.version_info[1] < 8:
        if "PATH" in os.environ:
            if lib_path in os.environ["PATH"]:
                pass
            else:
                os.environ["PATH"] += os.pathsep + lib_path
        else:
            os.environ["PATH"] = lib_path
    else:
        os.add_dll_directory(lib_path)

from .cmake_example import add, add_pi, subtract, divide
