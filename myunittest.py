import unittest
import coverage

# Start the coverage measurement
cov = coverage.Coverage()
cov.start()

# The function we want to test
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

class FactorialTestCase(unittest.TestCase):
    def test_factorial_positive(self):
        breakpoint()
        result = factorial(10)
        self.assertEqual(result, 3628800)
    
    def test_factorial_zero(self):
        result = factorial(0)
        self.assertEqual(result, 1)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

# Stop the coverage measurement and generate the report
cov.stop()
cov.save()
cov.html_report()

if __name__ == '__main__':
    unittest.main()