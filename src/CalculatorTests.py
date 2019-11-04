import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('src/UnitTestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(float(row['Value 1']), float(row['Value 2'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        test_data = CsvReader('src/UnitTestSubtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(float(row['Value 2']), float(row['Value 1'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        test_data = CsvReader('src/UnitTestMultiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(float(row['Value 1']), float(row['Value 2'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        test_data = CsvReader('src/UnitTestDivision.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.divide(float(row['Value 2']), float(row['Value 1'])), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        test_data = CsvReader('src/UnitTestSquare.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(float(row['Value 1'])), result)
            self.assertEqual(self.calculator.result, result)

    def test_squareroot_method_calculator(self):
        test_data = CsvReader('src/UnitTestSquareRoot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.squareroot(float(row['Value 1'])), result)
            self.assertAlmostEqual(self.calculator.result, result)

if __name__ == '__main__':
    unittest.main()
