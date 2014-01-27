def iterate(n):
	if (n % 2 == 0):
		return (n / 2)
	else:
		return ((3 * n) + 1)

starting_number = 999999
largest_length = 0

while(True):

	sequence = [starting_number]
	number = starting_number
	while(number != 1):
		number = iterate(number)
		sequence.append(int(number))
	
	if (largest_length < len(sequence)):
		largest_length = len(sequence)
		print(starting_number)
		print(largest_length)

	starting_number -= 1
	if (starting_number == 0):
		break
