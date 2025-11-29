import math
import time

class MathSeries:
    def __init__(self, n):
        if n < 0:
            raise ValueError("N must be a non-negative integer")
        self.n = n

    def fibonacci_iterative(self):
        """Iterative Fibonacci using object state"""
        a, b = 0, 1
        result = []
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        return result

    def fibonacci_series(self):
        """Original recursive Fibonacci - object method"""
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
        """Iterative factorial using object state"""
        value = 1
        for i in range(1, self.n + 1):
            value *= i
        return value

    def factorial(self):
        """Original recursive factorial - object method"""
        def helper(k):
            if k == 0 or k == 1:
                return 1
            return k * helper(k - 1)
        return helper(self.n)

    def factorial_math(self):
        """Math library factorial using object state"""
        return math.factorial(self.n)

    def time_method(self, method_name):
        """Object method to measure performance"""
        start = time.time()
        result = getattr(self, method_name)()
        end = time.time()
        return result, end - start

    def show_results(self):
        """Object method displaying all calculations"""
        print(f"\n=== MathSeries Object Results for N = {self.n} ===")
        
        fib_iter, t1 = self.time_method('fibonacci_iterative')
        fib_rec, t2 = self.time_method('fibonacci_series')
        fact_iter, t3 = self.time_method('factorial_iterative')
        fact_rec, t4 = self.time_method('factorial')
        fact_math, t5 = self.time_method('factorial_math')
        
        print(f"Fibonacci (iterative):  {fib_iter} [{t1:.6f}s]")
        print(f"Fibonacci (recursive): {fib_rec[:8]}... [{t2:.6f}s]")
        print(f"Factorial (iterative): {fact_iter:,} [{t3:.6f}s]")
        print(f"Factorial (recursive): {fact_rec:,} [{t4:.6f}s]")
        print(f"Factorial (math lib):  {fact_math:,} [{t5:.6f}s]")

# Pure object-oriented main program
n = int(input("Enter a positive integer N: "))
series = MathSeries(n)  # Create single object instance
series.show_results()   # All operations through object methods
