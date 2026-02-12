text = 'B[45]AB[9994]'

now = 0
ans = 0

while(True):
    start = text.find('[', now)
    end = text.find(']', now)

    if start == -1 or end == -1:
        break

    now = end + 1

    num = int(text[start + 1])

    for i in range(start+2, end):
        num = num * 10 + int(text[i])

    ans += num

print(ans)