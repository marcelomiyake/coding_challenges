#include "triangle.h"
#include <stdexcept>

namespace triangle {

    flavor kind(double sideA, double sideB, double sideC) {
        if (sideA >= sideB + sideC || sideB >= sideA + sideC || sideC >= sideA + sideB) {
            throw std::domain_error("");
        }
        if (sideA == sideB && sideB == sideC) {
            return flavor::equilateral;
        }
        if (sideA == sideB || sideB == sideC || sideC == sideA) {
            return flavor::isosceles;
        }
        return flavor::scalene;
    }

}  // namespace triangle
