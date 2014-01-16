x = 600851475143
num = 2
while num * num < x:
	if (x % num == 0):
		x = x / num
	num += 1
print(int(x))