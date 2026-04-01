from collections import deque

N, K = map(int, input().split())  # 수빈이가 있는 위치, 동생이 있는 위치
time = [float('inf')] * 100001


def bfs(now):
    queue = deque([now])
    time[now] = 0

    while queue:
        q = queue.popleft()

        if q == K:
            return time[q]

        for i in (2, 1, -1):
            # 2 * X 로 이동할 경우
            if i == 2:
                qq = q * 2
                # 방문 안한 위치만 방문
                if 0 <= qq <= 100000 and time[qq] > time[q]:
                    time[qq] = time[q]
                    queue.append(qq)
            # X-1 / X+1 로 이동할 경우
            else:
                qq = q + i
                if 0 <= qq <= 100000 and time[qq] > time[q]:
                    time[qq] = time[q] + 1
                    queue.append(qq)

print(bfs(N))