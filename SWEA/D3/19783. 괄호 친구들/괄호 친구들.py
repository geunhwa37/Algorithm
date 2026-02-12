arr = input()
start = 0
ans = 0

while(True):
    f1_start = arr.find('[', start)
    f1_end = arr.find(']', start)
    f2_start = arr.find('{', start)
    f2_end = arr.find('}', start)

    if f1_start == -1 and f2_start == -1:
        break
    elif f1_start == -1 and f2_start != -1:
        start = f2_end + 1

        num = int(arr[f2_start+1])
        for i in range(f2_start+2, f2_end):
            num *= 10
            num += int(arr[i])

        ans *= num

    elif f1_start != -1 and f2_start == -1:
        start = f1_end + 1

        num = int(arr[f1_start+1])
        for i in range(f1_start + 2, f1_end):
            num *= 10
            num += int(arr[i])

        ans += num
    else:
        if f1_start < f2_start:
            start = f1_end + 1

            num = int(arr[f1_start+1])
            for i in range(f1_start + 2, f1_end):
                num *= 10
                num += int(arr[i])

            ans += num
        else:
            start = f2_end + 1

            num = int(arr[f2_start+1])
            for i in range(f2_start + 2, f2_end):
                num *= 10
                num += int(arr[i])

            ans *= num

print(ans)