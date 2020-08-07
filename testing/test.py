import unittest
import main


class TestMain(unittest.TestCase):
    def test_calc(self):
        test_num1 = 10
        test_num2 = 20
        result = main.calculate(test_num1, test_num2)
        self.assertEqual(result, 30)

    def test_calc2(self):
        test_num1 = 10
        test_num2 = "aas"
        result = main.calculate(test_num1, test_num2)
        self.assertIsInstance(result, ValueError)


if __name__ == '__main__':
    unittest.main()
