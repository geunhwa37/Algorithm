
arr = ['Luffy', 'Zoro', 'Sanji']
path = []

def dfs(lev):

    # 종료조건
    if lev == 3:
        # 출력
        for i in range(3):
            if path[i] == 1:
                print(arr[i], end=' ')
        print()
        return

    for i in range(1, -1, -1):
        path.append(i)
        dfs(lev+1)
        path.pop()

dfs(0)