class MathSeries:
    def __init__(self, n):
        if n < 0:
            raise ValueError("N must be a non-negative integer")
        self.n = n

    def fibonacci_series(self):
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

        return helper(self.n)

    def factorial(self):
        def helper(k):
            if k == 0 or k == 1:
                return 1
            return k * helper(k - 1)
        return helper(self.n)


# main program
n = int(input("Enter a positive integer N: "))
math_series = MathSeries(n)

print("Fibonacci series:", math_series.fibonacci_series())
print("Factorial:", math_series.factorial())
