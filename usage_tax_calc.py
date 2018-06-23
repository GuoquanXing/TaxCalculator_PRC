from .income_tax_calc import IncomeTaxCalculator
from .five_i_one_f_calc import FiveInsuranceOneFundingCalculator


def salary_operation(raw_salary, city):
    my_5i1f_calc = FiveInsuranceOneFundingCalculator()
    print("debug:salary_operation-line7", city)
    taxable_salary, five_i_one_f_payable = my_5i1f_calc.calculate_taxable_salary_and_5i1f_payable(raw_salary=raw_salary, city=city)

    income_tax_calc = IncomeTaxCalculator()
    tax_payable = income_tax_calc.calculate_tax_payable(taxable_salary)

    actual_paid_salary = raw_salary - tax_payable - five_i_one_f_payable.get('Total')
    return tax_payable, five_i_one_f_payable, actual_paid_salary

