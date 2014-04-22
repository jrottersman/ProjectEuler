sum = 0
for num in xrange(1, 1000):
	if  num % 5 == 0:
		sum += num
	elif num % 3 == 0:
		sum +=num
print sum