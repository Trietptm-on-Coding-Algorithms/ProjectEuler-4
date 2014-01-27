def factorial_sum(n):
	total = n
	while(True):
		if (n == 1):
			break
		total *= n
		n -= 1
	return total

sum_of_digits = 0
number_list = list(str(factorial_sum(100)))

for num in range(0, len(number_list)):
	sum_of_digits += int(number_list[num])

print(sum_of_digits)