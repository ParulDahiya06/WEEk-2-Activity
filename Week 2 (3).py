

def fibonacci_series(n):
    # Recursive helper that returns list of first k Fibonacci numbers
    def helper(k):
        if k <= 0:
            return []
        if k == 1:
            return [0]
        if k == 2:
            return [0, 1]
        prev = helper(k - 1)
        prev.append(prev[-1] + prev[-2])
        return prev

    return helper(n)


def factorial(n):
    # Recursive factorial: n! = n * (n-1)!
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a number: "))

print("Fibonacci:", fibonacci_series(n))
print("Factorial:", factorial(n))
