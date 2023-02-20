#include "armstrong_numbers.h"
#include <stdio.h>

bool is_armstrong_number(int candidate) {
    int dividend = candidate;
    int exponent = 1;
    int digits[10];

    while (dividend / 10 > 0) {
        digits[exponent - 1] = dividend % 10;
        exponent++;
        dividend = dividend / 10;
    }
    digits[exponent - 1] = dividend;

    int sum = 0;
    for (int i = 0; i < exponent; i++) {
        int pow = 1;
        for (int j = 0; j < exponent; j++) {
            pow = pow * digits[i];
        }
        sum += pow;
    }
    return sum == candidate;
}
