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

    def calculate_all(self):
        """Convenience method to run all calculations"""
        results = {
            "fib_iterative": self.fibonacci_iterative(),
            "fib_recursive": self.fibonacci_recursive(),
            "fact_iterative": self.factorial_iterative(),
            "fact_recursive": self.factorial_recursive(),
            "fact_math": self.factorial_math()
        }
        return results


# Create object and use it
n = int(input("Enter a number: "))
calc = MathCalculator(n)

# Method calls on the object
print("Fibonacci (iterative):", calc.fibonacci_iterative())
print("Fibonacci (recursive):", calc.fibonacci_recursive())
print("Factorial (iterative):", calc.factorial_iterative())
print("Factorial (recursive):", calc.factorial_recursive())
print("Factorial (math):", calc.factorial_math())

# Or use the convenience method
print("\nAll results:", calc.calculate_all())
