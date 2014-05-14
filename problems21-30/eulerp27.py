def prime_sieve(stop):
	primes = [True] * stop
	primes[0], primes[1] = [False] * 2
	for ind, val in enumerate(primes):
		if val is True:
			primes[ind*2::ind] = [False] * (((stop - 1)//ind) - 1)
	return primes

P = prime_sieve(751000) #assuming the longest prime sequence is shorter than 500 this will work
a_m, b_m, c_m = 0, 0, 0
for a in range(-1000,1991):
	for b in range(1,1001):
		if P[b] is False: continue
		if b < -1600 -40*a or b< c_m: continue
		c, n = 0, 0
		while P[n**2 + a * n + b] is True:
			c += 1
			n += 1
		if c > c_m:
			a_m, b_m, c_m = a, b, c
answer = a_m * b_m
print answer