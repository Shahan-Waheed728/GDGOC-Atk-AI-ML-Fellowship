import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.5f} seconds")
        
        return result
    return wrapper


@execution_time
def sample_function():
    total = 0
    for i in range(1000000):
        total += i
    return total


if __name__ == "__main__":
    sample_function()