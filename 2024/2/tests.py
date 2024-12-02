import unittest
from main import solve2
import numpy as np

class Testcases(unittest.TestCase):
    def test_1(self):
        input = [1,2,3,4]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_2(self):
        input = [1,2,3,40]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    
    def test_3(self):
        input = [1,2,3,0]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))
    

    def test_4(self):
        input = [1,2,30,4]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_5(self):
        input = [1,20,3,4]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_6(self):
        input = [10,2,3,4]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_7(self):
        input = [1,5,3,4]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_8(self):
        input = [5,3,2,4]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_9(self):
        input = [1,20,40,3]
        correct = 0

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_10(self):
        input = [1,2,4,4]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_11(self):
        input = [1,30, 20,50]
        correct = 0

        self.assertEqual(correct, solve2([np.array(input)]))

    def test_12(self):
        input = [44, 44, 43, 40]
        correct = 1

        self.assertEqual(correct, solve2([np.array(input)]))





if __name__ == "__main__":
    unittest.main()
