from django.http import HttpResponse
from .tax_calc.usage_tax_calc import salary_operation

def index(request):
	parameters = request.GET
	raw_salary = parameters.getlist('raw_salary')
	city = parameters.getlist('city')

	raw_salary = float(raw_salary[0])
	tax_payable, five_i_one_f_payable, actual_paid_salary = salary_operation(raw_salary, city[0])
	str_title = '<h1>Given a raw salary ' + str(raw_salary) + ' in ' + city[0] + '</h1>'
	str_tax_payable =  '<li>应纳税额:' + str(tax_payable) + '</li>'
	str_5I1F_paybale = '<li>应扣除五险一金:' + str(five_i_one_f_payable) + '</li>'
	str_actual_paid_salary = '<li>实发工资:' + str(actual_paid_salary) + '</li>'
	response = HttpResponse()
	response.write(str_title)
	response.write(str_tax_payable)
	response.write(str_5I1F_paybale)
	response.write(str_actual_paid_salary)
	return HttpResponse(response)
