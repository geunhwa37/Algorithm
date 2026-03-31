from collections import deque

N, M = map(int, input().split()) # 학생 수, 키를 비교한 횟수

graph = [[] for _ in range(N+1)]
cnt = [0] * (N+1)

# 그래프 + 진입차수 세팅
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    cnt[B] += 1

# 큐 초기화 (진입차수 0) - 앞 사람 없는 사람부터 시작
queue = deque()
for i in range(1, N+1):
    if cnt[i] == 0: queue.append(i)

# 위상정렬
while queue:
    q = queue.popleft()
    print(q, end=' ')

    for i in graph[q]:
        cnt[i] -= 1
        if cnt[i] <= 0: queue.append(i)

