def sum_divisors(n):
    divs = [1]
    i = 2
    while (i*i < n):
        if (n%i == 0):
            divs.extend([i, n/i])
        i = i + 1
        
    # Perfect square case
    if (i*i == n):
        divs.append(i)
        
    return sum(divs)

N = 28124
sums = range(0, N)
abundants = []

for i in range(1, N):
    if (sum_divisors(i) > i):
        abundants.append(i)
        for j in abundants:
            if (i+j < N):
                sums[i+j] = 0

print sum(sums)