a = 2520
checkList = [11, 13, 14, 16, 17, 18, 19] #don't need to check 20 if we increment by 20
found = True
while (True):
	a += 20
	for x in checkList:
		if ((a % x) != 0):
			found = False
			break
		found = True
	if (found == True):
		break
print(a)