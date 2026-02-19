from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    visited = [False] * 100001
    queue = deque()
    queue.append((N, 0))  # (현재 위치, 시간)
    visited[N] = True

    while queue:
        x, time = queue.popleft()

        if x == K:
            return time

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))

print(bfs(N, K))
