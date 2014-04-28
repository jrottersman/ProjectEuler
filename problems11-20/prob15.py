def route_num(cube):
    L = [1] * cube
    for i in range(cube):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube - 1]

n = route_num(20)
print n