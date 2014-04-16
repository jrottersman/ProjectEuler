foo = 100
bar = 100
big = 0
while (foo <= 999 and bar <= 999):
	sum = foo * bar
	foo = foo + 1
	if foo == 999:
		bar = bar + 1
		foo = 100
	n = str(sum)
	if sum > big and n == n[::-1]:
		palindrome = n
		big = int(palindrome)
print big
