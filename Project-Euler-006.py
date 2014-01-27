sum_of_square = square_of_sum = sum_of_numbers = 0

for num in range(1, 101):
	sum_of_square += (num * num)
	sum_of_numbers += num

print((sum_of_numbers * sum_of_numbers) - sum_of_square)