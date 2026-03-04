import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘림

N = int(input())

arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
parent = [0] * (N+1)

# 입력 처리
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# dfs로 부모 노드 정하기
def dfs(n):
    visited[n] = 1

    for a in arr[n]:
        if not visited[a]:
            parent[a] = n
            dfs(a)

dfs(1)

# 부모 노드 번호 출력
for i in range(2, N+1):
    print(parent[i])