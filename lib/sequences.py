#!/usr/bin/env python3


def print_fibonacci(length):
    fib_list = [] # Create an empty list to store fibonacci numbers
    a, b = 0, 1 # Initialize the first two numbers of the sequence

    for _ in range(length):
        fib_list.append(a)  # Add the current Fibonacci number to the list
        a, b = b, a + b  # Update the Fibonacci numbers for the next iteration

    print(fib_list)

