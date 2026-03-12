N = int(input())
# index : 열
visited1 = [0] * 20
# index : / 방향 대각선
visited2 = [0] * 100
# index : \ 방향 대각선
visited3 = [0] * 100

cnt = 0

def check(y, x):
    if visited1[y] == 1 or visited2[y + x] == 1 or visited3[y - x + N] == 1:
        return False
    else:
        return True

def recur(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        # 가지치기 - 유망하지 않은 케이스 제외
        if check(col, row) == False: continue

        # visited배열에 기록
        visited1[col] = 1  # 열 방문처리
        visited2[col + row] = 1  # 왼쪽 대각선 방문처리
        visited3[col - row + N] = 1  # 오른쪽 대각선 방문처리

        recur(row + 1)

        # visited배열 기록 지우기 (백트래킹)
        visited1[col] = 0  # 열 방문처리
        visited2[col + row] = 0  # 왼쪽 대각선 방문처리
        visited3[col - row + N] = 0  # 오른쪽 대각선 방문처리
recur(0)
print(cnt)




