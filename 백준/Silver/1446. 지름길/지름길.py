import heapq

N, D = map(int, input().split()) # 지름길의 개수, 고속도로의 길이
graph = [[] for _ in range(D + 1)]

# 기본 도로 연결 (i → i+1)
for i in range(D):
    graph[i].append((i + 1, 1))

# 지름길 입력
for _ in range(N):
    start, end, dist = map(int, input().split()) # 지름길 시작 위치, 도착 위치, 지름길의 길이

    if end <= D:
        graph[start].append((end, dist))


distance = [float('inf')] * (D+1)
distance[0] = 0  # 초기값 설정!!!

# 다익스트라
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리됐던 노드면 무시
        if distance[now] < dist: continue

        for b, c in graph[now]:
            if distance[b] > dist + c:
                distance[b] = dist + c
                heapq.heappush(q, (dist + c, b))

dijkstra(0)

print(distance[D])