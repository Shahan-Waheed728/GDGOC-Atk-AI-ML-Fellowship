# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Custom Range Generator
def custom_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step


# Test
if __name__ == "__main__":
    print("Fibonacci:")
    for num in fibonacci(10):
        print(num, end=" ")

    print("\n\nCustom Range:")
    for num in custom_range(1, 10, 2):
        print(num, end=" ")