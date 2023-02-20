#include "hamming.h"
#include <string.h>

int compute(const char *lhs, const char *rhs) {
    int hammingDistance = 0;
    if (strlen(lhs) != strlen(rhs)) {
        return -1;
    }
    for (int i = 0; lhs[i] != '\0'; i++) {
        if (lhs[i] != rhs[i]) {
            hammingDistance++;
        }
    }
    return hammingDistance;
}