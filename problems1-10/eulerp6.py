y = 0
z = 0
for i in xrange(1,101):
	y = y + i * i
	z= z + i
z = z * z
solution = z - y
print solution