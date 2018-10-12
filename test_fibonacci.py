import unittest
from fibonacci import *

class MyUnitTest(unittest.TestCase):

    def test_fibonacci_Cing(self):
        self.assertEqual(fibonacci(5),5)

    def test_fibonacci_Six(self):
         self.assertEqual(fibonacci(6),8)

if __name__=='__main__':
    unittest.main()