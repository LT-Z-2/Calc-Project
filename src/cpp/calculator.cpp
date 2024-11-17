#include <pybind11/pybind11.h>

extern "C" {
    // asm func declarations
    float add(float a, float b) 
    float subtract(float a, float b)
    float multiply(float a, float b)
    float divide(float a, float b)
}

float add(float a, float b) {
    return add(a, b) // using asm func
}

float subtract(float a, float b) {
    return subtract(a, b)
}

float multiply(float a, float b) {
    return multiply(a, b)
}

float divide(float a, float b) {
    return divide(a, b)
}

PYBIND11_MODULE(calculator, m) {
    m.doc() = "Basic calculator module with C++ and asm integration";
    m.def("add")
    m.def("add")
    m.def("add")
    m.def("add")
}

