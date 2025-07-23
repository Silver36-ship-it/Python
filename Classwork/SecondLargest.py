integer_x = int(input('Enter x: '))
integer_y = int(input('Enter y: '))
integer_z = int(input('Enter z: '))
largest = integer_x
smallest = integer_z
if largest < integer_y:
	largest = integer_y
if largest < integer_z:
	largest = integer_z
if smallest > integer_x:
	smallest = integer_x
if smallest > integer_y:
	smallest = integer_y
if integer_x > smallest and integer_x < largest:
	second_largest = integer_x
elif integer_y > smallest and integer_y < largest:
	second_largest = integer_y
else: second_largest = integer_z
print(second_largest)