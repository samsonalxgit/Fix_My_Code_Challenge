#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated byspace.

    -For multiple of three print "Fizz" instead of the number and for multiples of five print "Buzz".
    -For numbers which are multiple of both three and five print "FizzBuzz".
    -Otherwise return the number itself
    """
    if n < 1:
        return

    temp_result = []
    for i in range(1, n+1):
        if(i % 15) ==0:
            temp_result.append("FizzBuzz")
        elif(i % 3) ==0:
            temp_result.append("Fizz")
        elif(i % 5) ==0:
            temp_result.append("Buzz")
        else:
            temp_result.append(str(i))
    print("".join(temp_result))


if __name__=='__main__':
    if len(sys.argv)<=1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)

