import itertools

def pythagorean_triple_candidate_test(a, b, c):
	if (c % 2 == 0): #c must be odd
		return False
	if ((a >= b) | (b >= c) | (a >= c)): #a < b < c
		return False
	if ((a % 3 != 0) & (b % 3 != 0)): #exactly one of a or b is divisible by 3
		return False
	if ((a % 3 == 0) & (b % 3 == 0)): #exactly one of a or b is divisible by 3
		return False
	if ((a % 4 != 0) & (b % 4 != 0)): #exactly one of a or b is divisible by 4
		return False
	if ((a % 4 == 0) & (b % 4 == 0)): #exactly one of a or b is divisible by 4
		return False
	if ((a % 5 != 0) & (b % 5 != 0) & (c % 5 != 0)): #exactly one of a or b or c is divisible by 5
		return False
	return True

def pythagorean_triple_test(a, b, c):
	if ((a * a) + (b * b) == (c * c)):
		return True
	return False

a = b = c = 100
listA = listB = listC = []

while (a < 500):
	listA.append(a)
	listB.append(b)
	listC.append(c)
	a += 1
	b += 1
	c += 1

permutations = itertools.product(listA, listB, listC)

pythagorean_triples = []
for perm in permutations:
	if (pythagorean_triple_candidate_test(perm[0], perm[1], perm[2]) == True):
		if (pythagorean_triple_test(perm[0], perm[1], perm[2]) == True):
			if (perm[0] + perm[1] + perm[2] == 1000):
				print(perm[0] * perm[1] * perm[2])
				break
