import time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time
n = 5
print("\nRecursive Algorithm Analysis:\n")
result, exec_time = measure_time(factorial, n)
print(f"Factorial of {n}: {result}, Execution time: {exec_time:.10f} seconds")
