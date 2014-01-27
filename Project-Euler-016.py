num = 2
for power in range(1, 1000):
	num = num * 2

number_list = list(str(num))

sum_of_digits = 0

for num in range(0, len(number_list)):
	sum_of_digits += int(number_list[num])

print(sum_of_digits)