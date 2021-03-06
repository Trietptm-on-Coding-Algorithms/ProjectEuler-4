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

x = 17
while (True):
	if (len(primes) > 10000):
		break
	else:
		if (primeTest(x) == True):
			primes.append(x)
		x += 2

print(primes[-1])
