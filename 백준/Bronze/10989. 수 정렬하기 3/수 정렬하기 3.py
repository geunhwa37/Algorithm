import sys

input = sys.stdin.readline # input()보다 훨씬 빠름
output = sys.stdout.write # print보다 훨씬 빠름

N = int(input())

# 카운팅 정렬 사용
arr = [0] * 10001

for _ in range(N):
    arr[int(input())] += 1

for i in range(1, 10001):
    for _ in range(arr[i]):
        output(str(i) + '\n')