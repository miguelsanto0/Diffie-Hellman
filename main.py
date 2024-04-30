# This is a sample Python script.
import math

import sympy
from sympy import *
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def mod_exp(x, y, N):

    if y == 0: return 1
    z = mod_exp(x, math.floor(y / 2), N)
    if y % 2 == 0:  # if y is even
        result = pow(z, 2)
        return result % N
    else:  # if y is odd
        result = x * pow(z, 2)
        return result % N

def generate_bit(bits):
    number = "1"

    for i in range(1, bits):

        number += "0"

    convert = int(number,2)
    return convert

def main():
    print("Generating prime p...")

    p = sympy.randprime(generate_bit(500), generate_bit(501))
    variable = False
    while not variable:
        if  sympy.isprime((p - 1) // 2):
            variable = True

        else:
            p = sympy.randprime(generate_bit(500), generate_bit(501))

    print(p)
    print("Generating a secure private exponent s...")
    s = random.randrange(generate_bit(500),generate_bit(501))
    print(s)
    print("Calculating exponent ")
    g = 5
    gsp = mod_exp(g, s, p)
    print(gsp)
    user_input = input("Enter g^b % p: ")
    password = mod_exp(int(user_input,10),s,p)
    print(password)
    print("Complete! ")

    # Use a breakpoint in the code line below to debug your script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
