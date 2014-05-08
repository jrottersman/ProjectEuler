import math


a = 1
b = 1
i = 2

while(True):
	c = a + b
	a = b
	b = c
	i += 1
	digits = int(math.log10(c)) + 1
	if digits >= 1000:
		print i
		break
		