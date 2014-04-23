import math

def Factors(n):
	num_factors = 0
	
	for i in range (1, int(math.sqrt(n))+1):
		if n% i == 0:
			num_factors += 1
	return (2 * num_factors)

n = 1
while(True):
	count = Factors(n*(n+1)/2)
	if count > 500:
		break
	n += 1
print n*(n+1)/2