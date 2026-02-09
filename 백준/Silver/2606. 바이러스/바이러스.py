c_num = int(input())  # 컴퓨터의 수
computer = int(input())  # 컴퓨터 쌍의 수

c = [[] for _ in range(c_num+1)]
for i in range(computer):
    a, b = map(int, input().split())
    c[a] += [b]
    c[b] += [a]

visited = [False] * (c_num + 1)

# dfs 함수
def dfs(x):
    if visited[x] == False:
        visited[x] = True
    else:
        return

    for i in c[x]:
        dfs(i)

dfs(1)
print(visited.count(True)-1)