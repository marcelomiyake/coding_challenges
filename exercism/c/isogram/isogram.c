#include "isogram.h"
#include <string.h>
#include <ctype.h>

bool is_isogram(const char phrase[]) {
    if (phrase == NULL) {
        return false;
    }
    if (phrase[0] == '\0') {
        return true;
    }
    for(int i = 0; phrase[i + 1] != '\0'; i++) {
        for (int j = i + 1; phrase[j] != '\0'; j++) {
            if(phrase[i] != ' ' && phrase[i] != '-' && tolower(phrase[i]) == tolower(phrase[j])) {
                return false;
            }
        }
    }
    return true;
}