#include <iostream>
#include <cmath>

int main() {

    float under = 1.0f;
    float over  = 1.0f;

    bool under_bool = false;
    bool over_bool = false;

    for (int i = 0; i <= 100000; i++) {

        if (over_bool == false) {
            over  = over * 2.0f;
        }

        if (under_bool == false) {
            under  = under / 2.0f;
        }        
        
        //std::cout << "Under: " << under << std::endl;
        
        if (under == 0.0f && under_bool == false) {
            std::cout << "Underflow reached at: " << i << std::endl;
            under_bool = true;
        }

        if (std::isinf(over) && over_bool == false) {
            std::cout << "Overflow reached at: " << i << std::endl;
            over_bool = true;
        }

        if (over_bool == true && under_bool == true) {
            break;
        }

    }
}