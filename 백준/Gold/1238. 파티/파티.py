import heapq

N, M, X = map(int, input().split()) # 학생 개수, 단방향 도로 개수, 파티 마을

graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, T = map(int, input().split()) # 도로의 시작점, 끝점, 소요시간
    graph[start].append((end, T))
    reverse_graph[end].append((start, T))  # 간선 반대로 저장

# 다익스트라
def dijkstra(start, gg):
    h = []
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    heapq.heappush(h, (0, start))

    while h:
        a, b = heapq.heappop(h)

        # 가지치기
        if distance[b] < a: continue

        for e, dist in gg[b]:
            cost = a + dist

            # 이미 처리된 경우 제외
            if distance[e] <= cost: continue

            distance[e] = cost
            heapq.heappush(h, (cost, e))

    return distance

# 가장 오래걸리는 학생 소요시간 구하기
# X -> 각 마을
go = dijkstra(X, graph)

# 각 마을 -> X
back = dijkstra(X, reverse_graph)

ans = 0
for i in range(1, N+1):
    ans = max(ans, go[i] + back[i])

print(ans)