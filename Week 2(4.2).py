import math

class MathCalculator:
    def __init__(self, n):
        if n < 0:
            raise ValueError("Enter a non-negative integer")
        self.n = n

    def fibonacci_iterative(self):
        a, b = 0, 1
        result = []
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        return result

    def fibonacci_recursive(self):
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

    def factorial_iterative(self):
        value = 1
        for i in range(1, self.n + 1):
            value *= i
        return value

    def factorial_recursive(self):
        if self.n == 0 or self.n == 1:
            return 1
        return self.n * self.factorial_recursive(self.n - 1)

    def factorial_math(self):
        return math.factorial(self.n)

    def display_results(self):
        """Display all calculations for this object"""
        print(f"\nResults for n = {self.n}:")
        print("Fibonacci (iterative):", self.fibonacci_iterative())
        print("Fibonacci (recursive):", self.fibonacci_recursive())
        print("Factorial (iterative):", self.factorial_iterative())
        print("Factorial (recursive):", self.factorial_recursive())
        print("Factorial (math):", self.factorial_math())


# Object-oriented usage
n = int(input("Enter a number: "))
calc = MathCalculator(n)  # Create object
calc.display_results()    # Call method on object
