def prime_finder(numbers):
    import numpy as np
    prime=np.array([])
    """will select only the prime #'s from a given numpy array"""
    for n in np.nditer(numbers):
        if (n%2)>0:
            prime = np.append(prime,n)
        return prime

    #a series of numbers in which each number ( Fibonacci number ) is the sum of the \n,
    #two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.\n,

def fibonacci_finder(numbers):
    """"will select only the Fibonacci numbers from a given numpy array."""
    import numpy as np
    fib_nums=np.array([])
    x=2 #index counter
    for n in np.nditer(numbers[2:]):
        if n == (numbers[x-1]+numbers[x-2]):
            fib_nums = np.append(fib_nums,n)
            x+=1
    return fib_nums