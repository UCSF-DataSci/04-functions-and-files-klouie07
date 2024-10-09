#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import argparse
from fibonnaci import fibonacci_generate

def prime_check(n):
    if n < 2:
        return False
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

def parser():
    parser = argparse.ArgumentParser(description='Finding largest prime Fibnacci number below certian number.')
    parser.add_argument('--limit', '-limit', type=int, default=10, help='Enter value limit')
    
    args = parser.parse_args()
    limit = args.limit
    
    fib_seq = fibonacci_generate(limit)
    
    prime_fib_seq = []
    for num in fib_seq:
        if prime_check(num):
            prime_fib_seq.append(num)
            
    if prime_fib_seq:
        largest_num = max(prime_fib_seq)
        print(f"Largest prime Fibonacci under {limit} is {largest_num}.")
    else:
        print(f"No prime Fibonacci numbers found.")

if __name__ == '__main__':
	parser()
