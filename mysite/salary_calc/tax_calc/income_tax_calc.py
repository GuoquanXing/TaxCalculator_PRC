import numpy as np


class IncomeTaxCalculator:
    __tax_rate_table_default = [[0, 0.03], [1500, 0.10], [4500, 0.20], [9000, 0.25], [35000, 0.3], [55000, 0.35], [80000, 0.45]]

    def __init__(self, tax_rate_table=None):
        """
        该应纳所得税计算器暂时只支持扣除五险一金后的工资额作为输入

        :param tax_rate_table: 累进税率表
        """
        # 初始化累进税率表
        if tax_rate_table is None:
            self.tax_rate_table = self.__tax_rate_table_default
        else:
            self.tax_rate_table = tax_rate_table
        # 计算速算扣除数,以数组的形式存储
        self.quick_deducting_amount = np.full(len(self.tax_rate_table), 0)
        for i in range(len(self.tax_rate_table)):
            if i == 0:
                self.quick_deducting_amount[0] = 0
            else:
                self.quick_deducting_amount[i] = self.quick_deducting_amount[i - 1] + self.tax_rate_table[i][0] * (
                        self.tax_rate_table[i][1] * 100 - self.tax_rate_table[i - 1][1] * 100) / 100

    def calculate_tax_payable(self, taxable_salary):
        """
        该方法适用于任何累进税率表,即累进税率表的更改不会影响该方法的正确性
        (modification-free in case the tax rate table is updated)
        
        :param taxable_salary: 应税收入额
        :return: 应纳税额
        """"""
        """
        tax_payable = 0

        if taxable_salary < 0:
            return -1

        range_levels = len(self.tax_rate_table)
        i = range_levels - 1
        while i < range_levels:
            if i < 0:
                break
            # determine which range the given salary amount locates in, descending order by amount
            if taxable_salary >= self.tax_rate_table[i][0]:
                # locate the tax rate for given range level and calculate the tax payable by formula:
                #  TaxPayable = (taxable_amount * tax_rate) - quick_deducted_amount
                range_level_tax_rate = self.tax_rate_table[i][1]
                tax_payable = taxable_salary * range_level_tax_rate - self.quick_deducting_amount[i]
                break
            else:
                i = i - 1
        return round(tax_payable, 2)