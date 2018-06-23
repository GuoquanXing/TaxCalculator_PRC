# PHF: 住房公积金 SI: 社会养老保险 HI: 医疗保险 BI: 生育保险  UI: 失业保险 :II:工伤保险
sh_5I1F_table = {'PHF': 7, 'SI': 8, 'HI': 2, 'BI': 0.1, 'UI': 0.5, 'II': 0.2}

five_I_One_F_table = {}
five_I_One_F_table.update({'SH': sh_5I1F_table})


def calculate_taxable_salary_and_5i1f_payable(raw_salary, city):
    PHFable = round(raw_salary * five_I_One_F_table.get(city).get('PHF') / 100, 2)
    SIable = round(raw_salary * five_I_One_F_table.get(city).get('SI') / 100, 2)
    HIable = round(raw_salary * five_I_One_F_table.get(city).get('HI') / 100, 2)
    BIable = round(raw_salary * five_I_One_F_table.get(city).get('BI') / 100, 2)
    UIable = round(raw_salary * five_I_One_F_table.get(city).get('UI') / 100, 2)
    IIable = round(raw_salary * five_I_One_F_table.get(city).get('II') / 100, 2)

    five_i_one_f_payable = {
        'PHFable': PHFable, 'SIable': SIable, 'HIable': HIable, 'BIable': BIable, 'UIable': UIable, 'IIable': IIable,
        'Total': round(PHFable + SIable + HIable + BIable + UIable + IIable, 2)
    }
    taxable_salary = round(raw_salary - PHFable - SIable - HIable - BIable - UIable - IIable, 2)
    return taxable_salary, five_i_one_f_payable


def add_new_five_i_one_f_table(city, five_i_one_f_table):
    if type(five_i_one_f_table) != dict:
        return
    else:
        five_I_One_F_table.update({city: five_i_one_f_table})
