primes = [2, 3, 5, 7, 11, 13]

def primeTest(num):
	if ((num % 2) == 0):
		return False
	if ((num % 3) == 0):
		return False
	x = 5
	while((x * x) <= (num + 1)): #don't go beyond sqrt of number to save time
		if (num % x == 0):
			return False
		x += 2 #ignore even numbers 
	return True

x = 17 #start on a known prime
total = 0
while (True):
	if (x > 2000000):
		break
	else:
		if (primeTest(x) == True):
			primes.append(x)
			total += int(prime)
		x += 2

print(total)

