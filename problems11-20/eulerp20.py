import math

factorial = math.factorial(100)

digits = map(int, str(factorial))
sum = 0
for i in range(len(digits)):
	sum += digits[i]
print sum