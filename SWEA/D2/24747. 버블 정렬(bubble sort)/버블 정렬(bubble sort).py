

arr = [12, 3, 9, 1, 15, 7]

def bubble_sort(a, N):
    for i in range(N-1, 0, -1):

        for j in range(0, i):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

    return a


print(*bubble_sort(arr, 6))