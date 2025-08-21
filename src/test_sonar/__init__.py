def fib(n):
    unused = 5

    if n < 0:
        raise ValueError(f"n must be >=0, got {n}")
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)
