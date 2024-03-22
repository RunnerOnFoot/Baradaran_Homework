# With the time complexity of O(n)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b


for i in range(100):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
