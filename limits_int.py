import sys
import numpy

print("-Python int has no fixed max/min, only limited by memory, manually inserted limits for 32 bit with numpy")

over = numpy.int32(2**31 - 10)
under = numpy.int32(-2**31 + 10)

under_bool = False
over_bool  = False

for i in range(10000):   # finite loop
    if over_bool == False:
        
        next_over = over + 1
        
        if next_over < over:
            print(f"Overflow reached with max int = {over}")
            over_bool = True
        
        over = next_over


    if under_bool == False:
        
        next_under = under - 1
        
        if next_under > under: 
            print(f"Underflow reached with min int = {under}")
            under_bool = True

        under = next_under

    
    if over_bool == True and under_bool == True:
        break


if over_bool == False:
    print(f"Current 'over' value:  {over}")
    print("No overflow found")

if under_bool == False:
    print(f"Current 'under' value: {under}")
    print("No underflow found")