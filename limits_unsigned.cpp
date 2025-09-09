#include <iostream>
#include <cmath>

int main() {
    
    // using numeric_limits to be able to complete loop and display max/min usigned int before wrapping
    
    unsigned int under = 10;
    unsigned int over  = std::numeric_limits<unsigned int>::max()-10;

    bool under_bool = false;
    bool over_bool = false;

    for (int i = 0; i <= 100000; i++) {

        if (over_bool == false) {
            
            int next = over + 1;

            if (next < over) {
                std::cout << "Overflow reached with max unsigned int = " << over << std::endl;
                over_bool = true;
            }

            over = next;
        }

        
        if (under_bool == false) {
            int next = under - 1;
            
            if (next > under) {
                std::cout << "'Underflow' reached with min unsigned int = " << under << std::endl;
                under_bool = true;
            }

            under = next;
        }        
        
        if (over_bool == true && under_bool == true) {
            break;
        }

    }
}