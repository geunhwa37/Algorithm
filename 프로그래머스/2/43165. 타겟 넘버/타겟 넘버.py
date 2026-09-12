def solution(numbers, target):
    
    def dfs(depth, now, ans):
        if depth == len(numbers):
            ans.append(now[:])
            return
        for i in [0,1]:
            now.append(i)
            dfs(depth+1, now, ans)
            now.pop()
    
    ans = []
    dfs(0, [], ans)
    
    answer = 0
    
    for a in ans:
        tt = 0
        for i in range(len(a)):
            if a[i] == 0 :
                tt -= numbers[i]
            else:
                tt += numbers[i]
        if tt == target: answer += 1
    
    return answer