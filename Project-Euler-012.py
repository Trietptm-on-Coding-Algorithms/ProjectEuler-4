#brute-force solution. Will probably take hours/days to run.

def add_triangle_number_sequence(length):
	if (length < 1):
		return None
	else:
		y = 0
		for x in range(1, length + 1):
			y += x
		return y


def find_and_count_divisors(number):
	if (number < 1):
		return None
	else:
		divisors = []
		for x in range(1, number + 1):
			if (number % x == 0):
				divisors.append(x)

		return divisors

divisors = 0
x = 5000
while (divisors <= 500):
	divisors = len(find_and_count_divisors(add_triangle_number_sequence(x)))
	print(str(x) + " " + str(divisors))
	x += 1

print(add_triangle_number_sequence(x - 1))