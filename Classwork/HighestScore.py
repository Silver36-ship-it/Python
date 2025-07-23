score_a = int(input('Enter score'))
score_b = int(input('Enter another score'))
score_c = int(input('Enter another score'))
highest = score_a
if score_b > score_a:
	highest = score_b
if score_c > score_b: 
	highest = score_c
print(highest)