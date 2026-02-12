arr = ['A', 'B', 'C', 'D', 'E']

path = []

def KFC(lev, start):
    # 종료 조건
    if lev == 3:
        print(*path)
        return
    # start로 조합 만들기
    for i in range(start, 5):
        path.append(arr[i])
        KFC(lev+1, i+1)
        path.pop()


KFC(0, 0)
