#include <iostream>
#include <cmath>

int main() {

    double under = 1;
    double over  = 1;

    bool under_bool = false;
    bool over_bool = false;

    for (int i = 0; i <= 100000; i++) {

        if (over_bool == false) {
            over  = over * 2;
        }

        if (under_bool == false) {
            under  = under / 2;
        }        

        if (under == 0 && under_bool == false) {
            std::cout << "Underflow reached at step: " << i << std::endl;
            under_bool = true;
        }

        if (std::isinf(over) && over_bool == false) {
            std::cout << "Overflow reached at step: " << i << std::endl;
            over_bool = true;
        }

        if (over_bool == true && under_bool == true) {
            break;
        }

    }
}