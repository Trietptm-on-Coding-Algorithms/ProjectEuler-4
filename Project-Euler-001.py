y = 0
for x in range(0, 1000):
	if ((x % 3 == 0) | (x % 5 == 0)):
		y += x
print(y)