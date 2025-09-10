# numrep

## Overflows and Underflows:

For multiplying/dividing by 2 in each iteration:

1. Float underflow occurs as iteration 149, and overflow occurs at iteration 127
2. Double underflow occurs as iteration 1074, and overflow occurs at iteration 1023

For adding 1 in each iteration:

3. Integer underflow reached with min int = -2147483648, and overflow at max int = 2147483647
4. Unsigned integer underflow reached with min int = 0, and overflow at max int = 4294967295
5. In python, built in int is arbitrary precision, limited by memory. Internally it grows to fit as many bits as needed. This behavior is shown in the limits_int.py and limits_unsigned.py

## Bessel:
Which method of calculating the bessel functions is more accurate?
1. According to the plots in bessel.png, both are very close. However, for J8 near x=0, the result using the up method is negative. This is incorrect; the down method captures the actual behavior, starting at a value of 0.

## Numerical Derivatives:
Check whether the number of decimal places obtained agrees roughly with the estimates in the text.
- The text estimates that the relative error for the forward method $\varepsilon_{fd} \sim 10^{-8}$ and central method $\varepsilon_{cd}\sim10^{-11}$.
- The text does not provide an estimate for the extrapolation method, but the result in the plots show roughly $10^{-13}$ for the t = 1, 0.1 cases, and $10^{-11}$ for the t = 100 case.

Do the slopes agree with our model’s predictions?
- Yes, the slopes match expectation. Forward is predicted to have $\varepsilon_{fd} \sim h$, central $\varepsilon_{cd} \sim h^2$, and extrapolated $\varepsilon_{ed} \sim h^4$, all of which align with the difference between $\varepsilon$ and $h$ shown in the results.
