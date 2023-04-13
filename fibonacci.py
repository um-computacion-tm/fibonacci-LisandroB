import unittest;

def Fibonacci(number):
    if number == 1:
        return number 
    return Fibonacci(number-2) + Fibonacci(number+2)

class testFibonacci(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1, Fibonacci(1))
        
if __name__ == '__main__':
    unittest.main();