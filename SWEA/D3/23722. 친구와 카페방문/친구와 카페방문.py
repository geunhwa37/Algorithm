arr = input().split()
n = len(arr)

# 오른쪽으로 밀면서 마지막 비트가 1인지 확인
def get_count(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1

    return cnt

result = 0
for tar in range(1 << n): # 2의 n제곱 (부분집합의 개수)
    if get_count(tar) >= 2: # 친구가 2명 이상
        result += 1

print(result)