nums = []
with open('prob13num.txt', 'r') as big:
	for num in big:
		nums.append(int(num))
total = (sum(nums))
print total