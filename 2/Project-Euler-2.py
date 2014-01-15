y = [1, 1]
for num in range(1, 100):
	x = y[num] + y[num - 1]
	if (x > 4000000):
		break
	y.append(x)

z = 0
for num in range(len(y)):
	if (y[num] % 2 == 0):
		z += y[num]
print(z)