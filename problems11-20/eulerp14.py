def collatz (i, count =1):
	while i >1:
		count += 1
		if i % 2 == 0:
			i = i / 2
		else:
			i = 3 * i + 1
	return count
	
max = [0, 0]
for j in range(1000000):
	foo = collatz(j)
	if foo > max[0]:
		max[0] = foo
		max[1] = j
print max[1]
	