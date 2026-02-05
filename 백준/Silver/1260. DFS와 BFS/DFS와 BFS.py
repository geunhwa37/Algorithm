from collections import deque

N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색 시작 정점 번호

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a] += [b]
    graph[b] += [a]

for i in range(N+1):
    graph[i].sort()

# 방문
visited_dfs = [False] * (N + 1)

# dfs 함수
def dfs(graph, V, visited_dfs):

    if visited_dfs[V] == False:
        visited_dfs[V] = True
        print(V, end=' ')

        for i in graph[V]:
            dfs(graph, i, visited_dfs)

# 방문
visited_bfs = [False] * (N + 1)

# bfs 함수
def bfs(graph, V, visited_bfs):
    queue = deque([V])

    visited_bfs[V] = True

    while queue:
        a = queue.popleft()
        print(a, end=' ')

        for i in graph[a]:
            if visited_bfs[i] == False:
                queue.append(i)
                visited_bfs[i] = True


dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
