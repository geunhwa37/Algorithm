import sys

sys.setrecursionlimit(10 ** 6) # limit 늘리기..

N = int(input())

arr = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
arr_new = [arr[i][:] for i in range(N)]
visited2 = [[False]*N for _ in range(N)]

#적록색약 리스트 만들기
for i in range(N):
    for j in range(N):
        if arr_new[i][j] == 'G': arr_new[i][j] = 'R'

# dfs 함수
def dfs(arr, y,x, visi):

    visi[y][x] = True

    for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
        yy = y + dy
        xx = x + dx

        if yy<0 or xx<0 or yy>=N or xx>=N or visi[yy][xx]: continue
        # 다른 색이면 탐색 안하기
        if arr[y][x] != arr[yy][xx]: continue

        dfs(arr, yy, xx, visi)

cnt1 = 0
cnt2 = 0
# 적록색약 아닌 사람
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(arr, i, j, visited)
            cnt1 += 1

# 적록색약인 사람
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            dfs(arr_new, i, j, visited2)
            cnt2 += 1

print(cnt1, cnt2)