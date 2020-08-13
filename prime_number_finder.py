import pandas as pd
import numpy as np
from mpmath import mp

mp.dps = 200
e = str(mp.e)
pi = str(mp.pi)
phi = str(mp.phi)
euler = str(mp.euler)
catalan = str(mp.catalan)
apery = str(mp.apery)
khinchin = str(mp.khinchin)
mertens = str(mp.mertens)

primes = []
def prime_check(start, end):
    for num in range(start, end + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:
                primes.append(str(num))

# x must be int, number must be string
def slow_check(number, x): #x is order of prime
    prime_check(10**(x-1), (10**x)-1)
    for z in range(mp.dps-1):
        if number[2+z:2+z+x] in primes:
            print(number[2+z:2+z+x])

def fast_check(number, x): # Change back to -2 and 2+
    for z in range(mp.dps - 2):
        num = int(number[2+z:2+z+x])
        if num > (10**(x-1)):
            for i in range(2, int((num/2)+1)):
                if (num % i) == 0:
                    break
            else:
                print(num)

    
def number_input():
    answer = input("""
    Select your number:
    A: Pi (π)
    B: Base of Natural Log (e)
    C: Golden Ratio (φ)
    D: Euler's Constant (γ)
    E: Catalan's Constant (G)
    F: Apéry's Constant (ζ(3))
    G: Khinchin's Constant (K0)
    H: Mertens' Constant (M)
    """)
    switcher = {
        "A": pi,
        "a": pi,
        "B": e,
        "b": e,
        "C": phi,
        "c": phi,
        "D": euler,
        "d": euler,
        "E": catalan,
        "e": catalan,
        "F": apery,
        "f": apery,
        "G": khinchin,
        "g": khinchin,
        "H": mertens,
        "h": mertens
    }
    return switcher.get(answer)


fast_check(number_input(), int(input("""
    What size prime numbers? (in digits)
    """)))