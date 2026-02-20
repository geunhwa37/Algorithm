from collections import deque
# N개의 필수과목 - 1~N
# 선수과목을 무조건 먼저 이수해야함
# 모든 과목을 완료하는 데 최소 몇 학기가 필요한지 계산하라
N, M = map(int, input().split())  # 과목의 수, 선수 조건의 수

# 그래프: A → B (A를 먼저 들어야 B를 들을 수 있음)
subject = [[] for _ in range(N+1)]

# indegree[i] = i 과목의 선수과목 개수
indegree = [0] * (N+1)

# 입력 처리
for _ in range(M):
    A, B = map(int, input().split())
    subject[A].append(B)
    indegree[B] += 1

# t[i] = i 과목을 들을 수 있는 최소 학기
t = [0] * (N+1)

# 큐 (위상정렬용)
queue = deque()

# 선수과목이 없는 과목은 바로 1학기에 들을 수 있음
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        t[i] = 1

# 위상정렬 시작
while queue:
    q = queue.popleft()

    # q를 선수과목으로 가지는 과목들 확인
    for s in subject[q]:
        indegree[s] -= 1
        # s를 들으려면 q를 먼저 들어야 하므로
        # q 다음 학기 = t[q] + 1
        #
        # 근데 s는 여러 선수과목이 있을 수 있음
        # → 그 중 가장 늦게 끝나는 과목 기준으로 해야함
        #
        # 그래서 max 사용
        t[s] = max(t[s], t[q]+1)

        # 선수과목이 모두 끝났다면
        if indegree[s] == 0:
            queue.append(s)  # 이제 들을 수 있음


for i in range(1, N + 1):
    print(t[i], end=' ')
