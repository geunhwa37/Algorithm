
arr = list(map(int, input().split()))

# 선택정렬 함수
def selection_sort(a, N):

    cnt = 0
    while cnt < N-1:
        min_arr = float('inf')
        min_index = None

        for i in range(cnt, N):
            if min_arr > a[i]:
                min_arr = a[i]
                min_index = i

        a[min_index], a[cnt] = a[cnt], a[min_index] # 교환
        cnt += 1
    return a

print(*selection_sort(arr, len(arr)))