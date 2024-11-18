from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# Define the extension module
ext_modules = [
    Pybind11Extension(
        "calculator",                      # Module name
        ["../cpp/calculator.cpp"],        # C++ source file
        extra_objects=["src/asm/basiccpu.o"], # Precompiled assembly object file
        extra_compile_args=["-std=c++17"], # C++17 support
    ),
]

# Setup function
setup(
    name="calculator",
    version="1.0",
    author="Your Name",
    description="Python bindings for calculator with C++ and assembly integration",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)