import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(4, 4), 16)
        self.assertEqual(self.calculator.result, 16)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(6, 2), 3)
        self.assertEqual(self.calculator.result, 3)

if __name__ == '__main__':
    unittest.main()
