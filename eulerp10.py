from math import sqrt

def isprime(test):
	return not any (test % i == 0 for i in range(3, int(sqrt(test)) + 2))
	
	
test_num = 3 
sum = 5

prime_count = 2 

for test_num in range(3, 1999999, 2): 

	test_num += 2 

	if(isprime(test_num)):
		x = test_num
		sum += x
print sum
