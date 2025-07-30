import math
def divide_or_square (number):
	number = float(number)
	if type(number) == str or number <= 0:
		raise ValueError
	elif number % 5 == 0: 
		return round(math.sqrt(number),2)
	else:
		return round(number % 5,2)
		
def future_investment(investment_amount,monthly_interestRate,years):
	if type(investment_amount) == str or type(monthly_interestRate) == str or type(years) == str:
		raise ValueError
	convert_to_months = years * 12
	interest_rate_conversion = monthly_interestRate / 100 
	future_investment_value = investment_amount * (1 + interest_rate_conversion)**convert_to_months
	return round(future_investment_value,2)
	
		
	  
