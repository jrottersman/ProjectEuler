# the highest number needed to search for is 352,294 
# since seven 9 to the five equals 413343 which only has
# six digits for a seven digit number

total = 0

for i in range(2, 352294):
	if sum(map(lambda n: int(n)**5, str(i))) == i:
		total += i

print total