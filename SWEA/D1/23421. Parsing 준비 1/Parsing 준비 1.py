def reverse(arr):
    for a in range(len(arr)):
        r = -(a+1)

        if arr[a] == arr[r]:
            continue
        else:
            return 0
    return 1

arr = input()

print(reverse(arr))

