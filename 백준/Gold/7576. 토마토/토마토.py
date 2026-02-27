from collections import deque

m, n = map(int, input().split())
arr =[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

start_list = []

def bfs(arr, start_list):
    que = deque(start_list)
    while que:
        i, j , day = que.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
                arr[ni][nj] = 1
                que.append((ni, nj, day +1))
    for row in arr:
        for r in row:
            if r == 0:
                return -1
    return day




for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            start_list.append((i, j, 0))
print(bfs(arr, start_list))