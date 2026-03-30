import heapq

cnt = 1

while True:
    N = int(input())  # 동굴의 크기
    if N == 0: break # 종료

    arr = [list(map(int, input().split())) for _ in range(N)]


    def dijkstra():
        h = []
        distance = [[float('inf')] * N for _ in range(N)]

        heapq.heappush(h, (arr[0][0], 0, 0))
        distance[0][0] = arr[0][0]

        while h:
            dist, y, x = heapq.heappop(h)
            # 가지치기
            if distance[y][x] < dist: continue

            for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
                yy = y + dy
                xx = x + dx

                if yy < 0 or xx < 0 or yy >= N or xx >= N: continue

                cost = dist + arr[yy][xx]
                if distance[yy][xx] > cost:
                    heapq.heappush(h, (cost, yy, xx))
                    distance[yy][xx] = cost

        return distance[N-1][N-1]

    print(f'Problem {cnt}: {dijkstra()}')
    cnt += 1