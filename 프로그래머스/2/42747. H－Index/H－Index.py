def solution(citations):
    lenn = len(citations)
    h_index = 0
    for i in range(1, lenn+1):
        cnt = 0
        for c in citations:
            if c >= i: 
                cnt += 1
        if cnt >= i: h_index = i
        
    return h_index