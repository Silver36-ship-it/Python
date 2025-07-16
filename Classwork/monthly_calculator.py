principal = int(input('Enter the principal amount,p:'))
interest_rate = float(input('Enter th rate of interest,r:'))
duration = int(input('Enter the duration of the loan,n:'))
percentage_monthly_rate = interest_rate / ( 100 * 12)
duration_in_month = duration * 12
calculate_numerator =  percentage_monthly_rate * (1 + percentage_monthly_rate)**duration_in_month
calculate_denomenator = (1 + percentage_monthly_rate)**duration_in_month - 1
monthly_mortgage = principal * (calculate_numerator / calculate_denomenator)
print('Monthly mortgage payment is ', monthly_mortgage)