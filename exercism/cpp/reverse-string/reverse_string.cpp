#include "reverse_string.h"

namespace reverse_string {

    string reverse_string(string value) {
        string reverse = "";
        for(unsigned int i = 0; i < value.length(); i++) {
            reverse.append(value, value.length() - 1 - i, value.length() - 1);
        }
        return reverse;
    }

}  // namespace reverse_string
