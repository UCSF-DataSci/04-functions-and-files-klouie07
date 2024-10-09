#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

fibseq = []

def fibonacci_generate(limit):
	a = 0
	b = 1
	while a < limit:
		fibseq.append(a)
		c = a + b
		a = b
		b = c

	return fibseq


def parserstuff():
    
	parser = argparse.ArgumentParser(description='Generate Fibonacci numbers less than specified limit and write them to file')
	parser.add_argument('--limit', '-limit', type=int, help='Upper limit for Fibonacci numbers', default=10)
	parser.add_argument('filename', type=str, help='Output file with Fiboncci numbers')

	args = parser.parse_args()
	limit = args.limit
	filename = args.filename
	
	fib_num_gen = fibonacci_generate(limit)

	try:
		with open(filename, 'w') as f:
			f.write((str(fib_num_gen)))
		print(f"Fibonacci numbers writen to {filename}.")
		
	except IOError:
		print(f"Error writing to file.")


if __name__ == "__main__":
	parserstuff()