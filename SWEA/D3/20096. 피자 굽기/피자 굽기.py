V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
K = int(input()) # 시작 정점의 번호

arr = [[]]

# 주어진 시작점에서 다른 모든 정점으로의 최단 경로 구하기
# 정점 V개 간선 E개
# u에서 v로 가는 가중치 w인 간선이 존재함
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수 있음

for i in range(E):
    u, v, w = map(int, input().split())