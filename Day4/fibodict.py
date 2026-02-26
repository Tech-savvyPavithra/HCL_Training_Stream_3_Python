def fib(n, cache={}):
    if n <= 1:
        return n
    
    # Check if value already computed
    if n in cache:
        return cache[n]
    
    # Store computed value in cache
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]

print(fib(10)) 