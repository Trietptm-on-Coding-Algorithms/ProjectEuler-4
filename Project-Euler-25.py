y = [1, 1]
for num in range(1, 1000000000):
	x = y[num] + y[num - 1]
	if (len(str(x)) >= 1000):
		break
	y.append(x)

print(len(y) + 1) 
