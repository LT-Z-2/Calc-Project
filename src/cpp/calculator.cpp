#include <pybind11/pybind11.h>
#include <cmath>

extern "C" {
    // asm func declarations
    float add(float a, float b);
    float subtract(float a, float b);
    float multiply(float a, float b);
    float divide(float a, float b);
}

float add_wrapper(float a, float b) {
    return add(a, b); // using asm func
}

float subtract_wrapper(float a, float b) {
    return subtract(a, b);
}

float multiply_wrapper(float a, float b) {
    return multiply(a, b);
}

float divide_wrapper(float a, float b) {
    if (b == 0) {
        throw std::runtime_error("Division by zero!");
    }
    return divide(a, b);
}

float c_pow(float a, float b) {
    return std::pow(a, b);
}

float c_sqrt(float a) {
    if (a < 0){
        throw std::runtime_error("Square root of a negative number!");
    }
    return std::sqrt(a);
}

PYBIND11_MODULE(calculator, m) {
    m.doc() = "Basic calculator module with C++ and asm integration";
    m.def("add", &add_wrapper, "adding two numbers");
    m.def("subtract", &subtract_wrapper, "subtracting two numbers");
    m.def("multiply", &multiply_wrapper, "multiplying two numbers");
    m.def("divide", &divide_wrapper, "dividing two numbers");
    m.def("pow", &c_pow, "exponentiation");
    m.def("sqrt", &c_sqrt, "square root");
}

