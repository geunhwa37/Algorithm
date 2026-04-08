
T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 섬의 개수
    X = list(map(int, input().split())) # 각 섬들의 X좌표
    Y = list(map(int, input().split())) # 각 섬들의 Y좌표
    E = float(input()) # 환경 부담 세율 실수

    arr = []

    # 2개 조합 -> 거리 구하기
    for i in range(N):
        for j in range(i+1, N):
            e = E * ((X[i]-X[j])**2 + (Y[i]-Y[j])**2)
            arr.append((e, i, j))

    # 비용순 정렬
    arr.sort()

    # 크루스칼
    parent = [i for i in range(N)]

    def Find(i):
        if parent[i] != i:
            parent[i] = Find(parent[i])
        return parent[i]


    def Union(A, B):
        rootA = Find(A)
        rootB = Find(B)

        if rootA == rootB: return
        parent[rootB] = rootA

    ans = 0

    for e, a, b in arr:
        # 이미 연결 됐다면 제외
        if Find(a) == Find(b): continue

        Union(a, b)
        ans += e

    print(f'#{tc} {round(ans)}')


