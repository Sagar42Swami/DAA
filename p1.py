# Recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example
n = 10
print("Recursive Fibonacci Sequence:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")
# Iterative approach
def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example
print("\nIterative Fibonacci Sequence:")
fibonacci_iterative(10)
