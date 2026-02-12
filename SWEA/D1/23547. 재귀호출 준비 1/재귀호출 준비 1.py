
def recru(i, j, n, m):
    if i > n or j > m:
        return
    else:
        print(i, j)
        if j == 3:
            recru(i+1, 1, n, m)
        recru(i, j+1, n, m)


recru(1, 1, 3, 3)