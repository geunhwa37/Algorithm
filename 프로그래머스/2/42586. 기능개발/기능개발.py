def solution(progresses, speeds):
    answer = []
    
    while progresses:
        # 하루 간 개발 
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # 배포 가능 확인 
        def confo(pprroo, cnt):
            if not pprroo : return cnt
            if pprroo[0] >= 100:       
                pprroo.pop(0)
                speeds.pop(0)
                return confo(pprroo, cnt+1)
            else: return cnt
            
        funCnt = confo(progresses, 0)
        if funCnt: answer.append(funCnt)
    return answer