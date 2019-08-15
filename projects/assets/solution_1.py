import math
from decimal import *

getcontext().prec= 2000
sqrt2 = Decimal(2).sqrt()

def solution(n):
    """
    This function will find the solution to the problem as described in readme.txt
    """
    dec_ans = rec_sol_fast(Decimal(n))
    return str(int(dec_ans))


def rec_sol_fast(n):
    """
    This is a recursive function which computes the problem
    This solution works by using the concept of Beatty sequences, which 
    when a single sequence is another's complement, they partition N (the natural numbers)
    This means that we can take the highest number we deal with (floor of sqrt2 * n)
    and remove from it the complementary series. 
    In this case, the complementary series is floor((2 + sqrt(2)) * n).
    I did some simple calculations, and got to this formula. 
    let m = highest number we deal with (floor(n*sqrt2))
        n = number of digits in primary series
        w = number of digits in complementary series
        
    The proof for the end formula can be found at the end of the program.
    """
    if n > Decimal(0): # prevent infinite recursion -- base case.
        m = n * sqrt2
        m = m.to_integral_exact(ROUND_FLOOR)
        mint = int(m)

        w = Decimal(n)
        w = w * (sqrt2 - Decimal(1))
        w = w.to_integral_exact(ROUND_FLOOR)
        wint = int(w)
        
        sum_m = (mint * (mint + 1)) >> 1
        sum_2w = (wint * (wint + 1))
        return sum_m - sum_2w - rec_sol_fast(w)
    
    return 0


    
# print(solution(5))
# print(solution(77))
# print(solution(9**123)


# Here is found the proof for the formula in the end of rec_sol:
# Notation: .| n |.  means FLOOR of n
#           SN[ ... ] means SERIES FROM 0 TO N of interior -- example: S10[n] = 1 + 2 + 3 ... 10
# let A and B be two irrational numbers which are complementary.
# This means that 1/A + 1/B = 1

# By the definition of a Beatty sequence, https://en.wikipedia.org/wiki/Beatty_sequence
# this means that Sinf[.|A * n|.] and Sinf[.|B * n|.] partition the natural numbers.
# so, every number in the sequence .|1/A * n|. is not in the other sequence, and vice versa.
# And, every number in N is in either one of the two sequences.

# So, {seq A} union {seq B} == N
#     {seq A} intersection {seq B} == empty set.

# let:
#     m = .|A * n|.  || This is the highest number reached in our computation.
#                    || Note that m - n is the number of digits in series B, by
#                    || the fact that they partition n, and we removed the digits of n.

#     w = m - n      || This is the number of digits in series B.

# So, to go on with our proof.
# We've already determined that the summation of the two series adds to N, so:

# SN[.|A * n|.] + Sw[.|B * n|.] = m * (m + 1)/2

# SN[.|A * n|.] = m * (m + 1)/2 - Sw[.|B * n|.]

# Let's sub in our values for A and B.
# A = Sqrt(2).
# B = 2 + sqrt(2).
# to verify this is accurate:

# = 1/sqrt(2) + 1/(2 + sqrt(2))
# = ((2 + sqrt(2)) + sqrt(2)) / (sqrt(2) * (sqrt(2) + 2))
# = (2 + 2 * sqrt(2)) / (2 + 2 * sqrt(2))
# = 1

# Now, we know that the two series add up to the summation till m.

# SN[.|sqrt2 * n|.] = m * (m + 1)/2 - Sw[.|(2 + sqrt2) * n|.]

# Note we can split up the second series into:
# SN[.|sqrt2 * n|.] = m * (m + 1)/2 - 2*(w * (w + 1))/2 - Sw[.|sqrt2 * n|.]

# Now, notice that this is exactly the formula used as the return value for rec_sol.
