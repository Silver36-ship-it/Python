number_of_day = int(input('Enter n: '))
if number_of_day == 1:
	print('Monday')
if number_of_day == 2:
	print('Tuesday')
if number_of_day == 3:
	print('Wednesday')
if number_of_day == 4:
	print('Thursday')
if number_of_day == 5:
	print('Friday')
if number_of_day == 6:
	print('Saturday')
if number_of_day == 7:
	print('Sunday')
if number_of_day > 7 or number_of_day < 1:
	print('Invalid input')