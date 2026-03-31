from collections import deque

N, M = map(int, input().split()) # 학생 수, 키를 비교한 횟수

graph = [[] for _ in range(N+1)]
cnt = [float('inf')] + [0] * N

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    cnt[B] += 1

# 앞 사람 없는 사람부터 시작
queue = deque()
for i in range(1, N+1):
    if cnt[i] == 0: queue.append(i)

while queue:
    q = queue.popleft()
    print(q, end=' ')

    for i in graph[q]:
        cnt[i] -= 1
        if cnt[i] <= 0: queue.append(i)

