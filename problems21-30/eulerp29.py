terms = []
for a in range(2, 101):
	for b in range(2,101):
		z = a**b
		terms.append(z)
print len(set(terms))
	