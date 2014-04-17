from math import sqrt

def isprime(test):
	return not any (test % i == 0 for i in range(3, int(sqrt(test)) + 2)) #only return numbers
	#where there is a remainder when divided by any odd number between 3 and sqrt of number
	#factors can't be higher then sqrt of number and be an integer
	# no need to check evens because of how we use the formulas below
	
test_num = 3 # where we begin testing

prime_count = 2 # count number of primes since we are starting at 3 which is 2nd prime

while(prime_count < 10001): # break at 10001 prime

	test_num += 2 #exclude evens

	if(isprime(test_num)):
		prime_count += 1 #count primes
print test_num
	