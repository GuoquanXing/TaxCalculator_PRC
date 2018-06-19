import unittest
from income_tax_calc import IncomeTaxCalculator


class IncomeTaxCalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = IncomeTaxCalculator()
        print('累进税率表：', self.calculator.tax_rate_table)
        print('速算扣除数：', self.calculator.quick_deducting_amount)

    def tearDown(self):
        del self.calculator

    def test_calcluate_tax_payable(self):
        self.assertEqual(self.calculator.calculate_tax_payable(1500.00), 45.00)
        self.assertEqual(self.calculator.calculate_tax_payable(3000.00), 195.00)
        self.assertEqual(self.calculator.calculate_tax_payable(5000.00), 445.00)
        self.assertEqual(self.calculator.calculate_tax_payable(8000.00), 1045.00)
        self.assertEqual(self.calculator.calculate_tax_payable(12500.26), 2120.06)
        self.assertEqual(self.calculator.calculate_tax_payable(39500.98), 9095.29)
        self.assertEqual(self.calculator.calculate_tax_payable(75413.65), 20889.78)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(IncomeTaxCalculatorTestCase('test_calcluate_tax_payable'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())