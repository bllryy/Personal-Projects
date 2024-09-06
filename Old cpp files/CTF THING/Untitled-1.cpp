#include <iostream>

int main() {
    int x = 5;
    int y = 0;

    int result;
    try {
        result = x / y;
    } catch (...) {
        std::cout << "Error: Division by zero occurred!" << std::endl;
        std::cout << "Flag: CTF{cant_divide_by_zero}" << std::endl;
        return 1; // Exit with error code indicating the error
    }

    std::cout << "Result: " << result << std::endl;

    return 0;
}
