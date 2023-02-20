#if !defined(TRIANGLE_H)
#define TRIANGLE_H

namespace triangle {

    enum class flavor {
        equilateral, isosceles, scalene
    };

    flavor kind(double sideA, double sideB, double sideC);

}  // namespace triangle

#endif // TRIANGLE_H