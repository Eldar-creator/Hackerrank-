BAKTYBEKOV ELDAR

TEACHER, THESE CODES WORKS IN HACKERRANK , BUT DOES NOT WORK IN COLAB,
PAY ATTENTION.

1)Special Multiple
import math
import os
import random
import re
import sys

def solve(n):
    for i in range(1, 10**5):
        x = bin(i)[2:].replace("1", "9")   
        if int(x)%n==0: return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close() 







2)Die Hard 3 

import math
import os
import random
import re
import sys
def solve(a, b, c):
    from math import gcd
    if c > max(a,b):
        return "NO"
    elif not c % gcd(a,b):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        c = int(first_multiple_input[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()








    
3)Tell the Average
N, L = int(input()), [int(n) for n in input().split()]
while len(L) > 1:
    L[0] += L[1] + L[0] * L[1]
    L.pop(1)
print(L[0] % 1000000007)

