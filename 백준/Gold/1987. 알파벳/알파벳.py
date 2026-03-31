import sys

input = sys.stdin.readline

R, C = map(int, input().split()) # 세로 R, 가로 C
arr = [input().strip() for _ in range(R)]

ans = 0

visited = set()  # 상태 캐싱용

def dfs(y, x, bit, depth):
    global ans

    # 상태 중복 제거
    if (y, x, bit) in visited:
        return
    visited.add((y, x, bit))

    ans = max(ans, depth)

    # 가지치기 - 알파벳 26개 다 사용할 경우
    if ans == 26:
        return

    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny = y + dy
        nx = x + dx

        if 0 <= ny < R and 0 <= nx < C:
            idx = ord(arr[ny][nx]) - 65

            # 비트마스크 체크 - 시간 줄이기
            if not (bit & (1 << idx)):
                dfs(ny, nx, bit | (1 << idx), depth + 1)

# 시작
start = 1 << (ord(arr[0][0]) - 65)
dfs(0, 0, start, 1)

print(ans)