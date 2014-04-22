from fractions import gcd #import gcd tool

def lcm(a,b): # return lowest common multiple
	return (a * b) // gcd(a, b) #only checks a pair would be more efficient to do a loop with multiples
	#but lack of skill
	
foo = lcm(20,16) #first even check
bar = lcm(foo, 12) #last unique even
oddz = 3
while (oddz < 20): #loop to check the odd numbers
	baz = lcm(bar, oddz)
	if baz > bar: #resets lcm for high numbers
		bar = baz
	oddz += 2
print baz

