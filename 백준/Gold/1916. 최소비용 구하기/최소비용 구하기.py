import heapq

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

graph = [[] for _ in range(N+1)]

for _ in range(3, M+3):
    s, e, d = map(int, input().split()) # 출발 도시, 도착 도시, 버스 비용
    graph[s].append((e, d))

start, end = map(int, input().split()) # 출발점, 도착점

distance = [float('inf')] * (N+1)

# 다익스트라
def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0

    while h:
        dist, now = heapq.heappop(h)

        # 처리된 적 있는 노드라면 무시
        if distance[now] < dist: continue

        for a, b in graph[now]:
            cost = dist + b
            if cost < distance[a]:
                heapq.heappush(h, (cost, a))
                distance[a] = cost

dijkstra(start)

print(distance[end])