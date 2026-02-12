T = int(input())

for tc in range(1, T+1):

    arr = input()
    ans = []

    # 스택 사용
    for i in arr:
        if not(ans):
            ans.append(i)
            continue
        if ans[-1] == i:
            ans.pop()
        else:
            ans.append(i)
    print(f'#{tc} {len(ans)}')