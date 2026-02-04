def counting_sort(arr):
    k = 15 # 입력의 최대수
    lenArr = len(arr) # 입력 배열의 길이
    temp = [0] * lenArr
    counts = [0] * (k + 1)

    # count
    for i in range(lenArr):
        counts[arr[i]] += 1

    # 누적합
    for j in range(1, k + 1):
        counts[j] += counts[j - 1]

    # 뒤에서부터 배치
    for a in range(lenArr - 1, -1, -1):
        counts[arr[a]] -= 1
        temp[counts[arr[a]]] = arr[a]

    return temp


arr = [12, 3, 9, 1, 15, 7]
print(*counting_sort(arr))
