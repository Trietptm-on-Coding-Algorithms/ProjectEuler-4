import itertools

def palindromeTest(x, y):
	s = str(x * y)
	start = s[-int(len(s) / 2):]
	end = s[:int(len(s) / 2)]
	if (start == end[::-1]): #string reversal
		return x * y
	return None

a = 999
b = 999
limit = a - 100

palindromes = []
listA = []
listB = []
while (a > limit):
	listA.append(a)
	listB.append(b)
	a -= 1
	b -= 1

#cartesian product
permutations = list(itertools.product(listA, listB))

for pair in permutations:
	result = palindromeTest(pair[0], pair[1])
	if (result != None):
		palindromes.append(result)

print(max(palindromes))
