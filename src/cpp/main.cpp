#include <cmath>
#include <iostream>

// steps to compile and link: 
// - as -arch arm64 math_operations.asm -o math_operations.o  (arm-based macOS)
// - g++ -c main.cpp -o main.o
// - g++ -arch arm64 -o program cpp/main.cpp asm/math_operations.o -lm


// rosetta has intel emulation (something to think about)

// function linking and declaration
extern "C" {
    float add(float a, float b);
    float subtract(float a, float b);
    float multiply(float a, float b);
    float divide(float a, float b);
}

float _add(float a, float b);
float _subtract(float a, float b);
float _multiply(float a, float b);
float _divide(float a, float b);
float c_pow(float a, float b);
float c_sqrt(float a);


float _add(float a, float b) {
    return add(a, b);
}

float _subtract(float a, float b) {
    return subtract(a, b);
}

float _multiply(float a, float b) {
    return multiply(a, b);
}

float _divide(float a, float b) {
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

int main() {
    std::string op;
    float a, b;

    // Taking input
    //std::cout << "Enter first number: ";
    std::cin >> a;

    //std::cout << "Enter operation (+, -, *, /, ^, sqrt): ";
    std::cin >> op;

    // Check if operation is "sqrt"
    if (op == "sqrt") {
        std::cout << c_sqrt(a) << std::endl;
    } else {
        //std::cout << "Enter second number: ";
        std::cin >> b;

        if (op == "+") {
            std::cout << _add(a, b) << std::endl;
        } else if (op == "-") {
            std::cout << _subtract(a, b) << std::endl;
        } else if (op == "*") {
            std::cout << _multiply(a, b) << std::endl;
        } else if (op == "/") {
            if (b == 0) {
                std::cerr << "Error: Division by zero is not allowed." << std::endl;
            } else {
                std::cout << _divide(a, b) << std::endl;
            }
        } else if (op == "^") {
            std::cout << c_pow(a, b) << std::endl;
        } else {
            std::cerr << "Error: Invalid operation." << std::endl;
        }
    }

    return 0;
}