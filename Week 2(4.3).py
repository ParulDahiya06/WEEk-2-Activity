import math
import time

class MathSeries:
    def __init__(self, n):
        """Initialize object with n and empty results cache"""
        if n < 0:
            raise ValueError("N must be a non-negative integer")
        self.n = n
        self.results = {}  # Cache for computed results
        self.timings = {}  # Cache for execution times

    def fibonacci_iterative(self):
        """Iterative Fibonacci - stores result in self.results"""
        a, b = 0, 1
        result = []
        for _ in range(self.n):
            result.append(a)
            a, b = b, a + b
        self.results['fib_iter'] = result
        return result

    def fibonacci_series(self):
        """Recursive Fibonacci - uses self.n from __init__"""
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
        result = helper(self.n)
        self.results['fib_rec'] = result
        return result

    def factorial_iterative(self):
        """Iterative factorial using self.n"""
        value = 1
        for i in range(1, self.n + 1):
            value *= i
        self.results['fact_iter'] = value
        return value

    def factorial(self):
        """Recursive factorial using helper function"""
        def helper(k):
            if k == 0 or k == 1:
                return 1
            return k * helper(k - 1)
        result = helper(self.n)
        self.results['fact_rec'] = result
        return result

    def factorial_math(self):
        """Math library factorial"""
        result = math.factorial(self.n)
        self.results['fact_math'] = result
        return result

    def time_method(self, method_name):
        """Time execution using self.timings cache"""
        if method_name in self.results:
            return self.results[method_name], self.timings[method_name]
        
        start = time.time()
        result = getattr(self, method_name)()
        end = time.time()
        self.timings[method_name] = end - start
        return result, self.timings[method_name]

    def debug_state(self):
        """Debug method - shows self object state"""
        print(f"\n=== DEBUG: Object State ===")
        print(f"self.n = {self.n}")
        print(f"self.results keys: {list(self.results.keys())}")
        print(f"self.timings keys: {list(self.timings.keys())}")
        print(f"Total cached results: {len(self.results)}")

    def show_results(self):
        """Display results using cached object state"""
        print(f"\n=== MathSeries Results for N = {self.n} ===")
        
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

# Main program demonstrating self usage
n = int(input("Enter a positive integer N: "))
series = MathSeries(n)  # __init__ called here
print("Object created successfully")

series.debug_state()  # Show initial self state
series.show_results()  # All methods use self.n, self.results
series.debug_state()  # Show final self state after computations
