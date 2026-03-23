import heapq

N, E = map(int, input().split()) # 정점의 개수, 간선의 개수

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split()) # a,b 양방향 길, c=거리
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split()) # 반드시 거쳐야 하는 정점

# 다익스트라
def dijkstra(start):
    d = [float('inf')] * (N + 1)
    h = []
    heapq.heappush(h, (0, start))
    d[start] = 0

    while h:
        dist, now = heapq.heappop(h)

        if d[now] < dist: continue

        for a, b in graph[now]:
            cost = dist + b
            if cost < d[a]:
                heapq.heappush(h, (cost, a))
                d[a] = cost
    return d

# 시작점별 다익스트라 수행
dist_1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

# 1 ~ v1 까지의 최단 거리 + v1 ~ v2 최단거리 + v2 ~ N
sum1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
# 1 ~ v2 까지의 최단 거리 + v2 ~ v1 최단거리 + v1 ~ N
sum2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]

ans = min(sum1, sum2)

# 경로가 없을 경우에는 -1 출력
if ans < float('inf'):
    print(ans)
else: print(-1)