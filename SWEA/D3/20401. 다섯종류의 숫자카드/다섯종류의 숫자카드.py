arr = input()

cnt = 0

def dfs(now, arr):
    global cnt

    # 종료 조건
    if len(now) == 4:
        # 전에 뽑았던 카드번호와 간격이 3이상 차이나는 경우, 카운트 안함
        for i in range(3):
            if abs(int(now[i]) - int(now[i+1])) > 3:
                return
        cnt += 1
        return

    for a in arr:
        dfs(now+a, arr)

dfs("", arr)

print(cnt)