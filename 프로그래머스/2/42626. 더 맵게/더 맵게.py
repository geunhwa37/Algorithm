import heapq
def solution(scoville, K):
    
    h = []
    
    
    for s in scoville:
            heapq.heappush(h, s)
    def dd():
        answer = 0
        
        while True:
            
            first = heapq.heappop(h)
            if first >= K: return answer
            if len(h) < 1: return -1    
            second = heapq.heappop(h)
            nxt = first + second * 2
            heapq.heappush(h, nxt)
            answer += 1
        
    return dd()