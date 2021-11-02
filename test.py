from main import sockMerchant
import unittest

class Test(unittest.TestCase):
    def test_case_one(self):
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20, 30, 10, 20, 20, 10, 10, 30, 50, 10, 20, 30, 5, 8, 4, 15, 40, 60, 100, 42, 78, 54]
        n = 30
        result = 10
        self.assertEqual(sockMerchant(n, ar), result)

    def test_case_two(self):
        ar = [42, 42, 42, 42, 42, 42, 42, 42, 18, 42, 42, 42, 42, 42, 42, 42, 16, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
         42, 42, 42, 42, 42, 42, 90, 42, 42, 42, 20, 42, 85, 42, 42, 42, 42, 42, 40, 42, 42, 10, 42, 42, 20, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
          42, 42, 32, 42, 42, 42, 42]
        n = 80
        result = 36
        self.assertEqual(sockMerchant(n, ar), result)

if __name__ == '__main__':
    unittest.main()


