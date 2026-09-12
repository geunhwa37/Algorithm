from collections import deque
def solution(maps):
    n = len(maps) # 세로
    m = len(maps[0]) # 가로
    visited = [[0] * m for _ in range(n)]
    
    def bfs():
        queue = deque([(0,0)])
        visited[0][0] = 1
        
        while queue:
            y, x = queue.popleft()
            if y == n-1 and x == m-1: return visited[n-1][m-1]
            
            for dy, dx in [(0,1), (1,0), (0,-1), (-1,0)]:
                yy = y + dy
                xx = x + dx 
                if yy < 0 or xx < 0 or yy >= n or xx >= m or maps[yy][xx] == 0 or visited[yy][xx] > 0: continue
                visited[yy][xx] = visited[y][x] + 1
                queue.append((yy, xx))
        
        return -1
    
    return bfs()