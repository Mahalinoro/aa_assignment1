from sockMerchant import sockMerchant
import unittest

class Test(unittest.TestCase):
    def test_30(self):
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20, 30, 10, 20, 20, 10, 10, 30, 50, 10, 20, 30, 5, 8, 4, 15, 40, 60, 100, 42, 78, 54]
        self.assertEqual(sockMerchant(30, ar), 10)

    def test_80(self):
        ar = [42, 42, 42, 42, 42, 42, 42, 42, 18, 42, 42, 42, 42, 42, 42, 42, 16, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
         42, 42, 42, 42, 42, 42, 90, 42, 42, 42, 20, 42, 85, 42, 42, 42, 42, 42, 40, 42, 42, 10, 42, 42, 20, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42, 42,
          42, 42, 32, 42, 42, 42, 42]
        self.assertEqual(sockMerchant(80, ar), 36)

if __name__ == '__main__':
    unittest.main()


