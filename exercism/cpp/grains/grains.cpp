#include "grains.h"
#include <math.h>

namespace grains {
    unsigned long long square(long value) {
        return pow(2, value - 1);
    }

    unsigned long long total() {
        long long sum = 0;
        for (int i = 1; i <= 64; i++) {
            sum += square(i);
        }
        return sum;
    }

}  // namespace grains
