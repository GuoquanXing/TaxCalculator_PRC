import unittest
from five_i_one_f_calc import calculate_taxable_salary_and_5i1f_payable


class FiveIOneFTestCase(unittest.TestCase):
    def test_calculate_5i1f_payable(self):
        taxable_salary, five_i_1_f_payable = calculate_taxable_salary_and_5i1f_payable(12345, 'SH')
        self.assertEqual(taxable_salary, 10147.58)
        self.assertEqual(five_i_1_f_payable.get('Total'), 2197.42)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(FiveIOneFTestCase('test_calculate_5i1f_payable'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())