# Script to print Fibonacci sequence up to n-th term

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

# Let's say we want the first 10 terms
n = 10
print(f"First {n} terms of Fibonacci sequence: {fibonacci(n)}")
