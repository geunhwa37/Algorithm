T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]

    # 완전탐색 - 재귀
    # dept = 7
    def rec(dep, y, x, temp):
        # 종료 조건
        if dep == 7:
            t.append(''.join(temp))
            return

        for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
            yy = y + dy
            xx = x + dx

            if yy<0 or xx<0 or yy>=4 or xx>=4: continue
            temp.append(str(arr[yy][xx]))
            rec(dep+1, yy, xx, temp)
            temp.pop()


    # 완전탐색
    ans = []
    for i in range(4):
        for j in range(4):
            temp = []
            t = []
            rec(0, i, j, temp)
            for k in t:
                if k not in ans:
                    ans.append(k)


    print(f'#{tc} {len(ans)}')
