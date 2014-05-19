def sum_diagonals(size):
	n = 1
	step  = 2
	total = 0
	last = 0
	while n <= size ** 2:
		total += n
		n += step
		last += 1
		if last == 4:
			step += 2
			last = 0
	return total
		
print sum_diagonals(1001)