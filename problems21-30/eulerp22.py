from string import ascii_uppercase

def total(word):
	return sum(ascii_uppercase.index(c) + 1 for c in word.strip('"')) #index starts at zero gets rid of quotes
	
	
f = open("c:/scripts/newdir/euler/names.txt", 'r')
names = f.read().split(',') #split by a comma
names.sort() #sorts the names alphabetically using pythons timsort
print sum (i*total(x) for i, x in enumerate(names, 1)) #iterate through the list of names and multiply by names score and the position with the x