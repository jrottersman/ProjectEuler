a = 0
b = 1
sum = 0
while (sum < 4000000):
	c = a + b
	a = b
	b = c
	if c % 2 == 0:
		sum = sum + c
	print sum
		