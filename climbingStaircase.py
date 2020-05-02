def climbingStaircase(n, k):
    
    if n == 0:
        return [[]]
    s = [[x] for x in range(1,k+1)]
    r = []
    
    while s:
        c = s.pop()
        
        if sum(c) == n:
            r.append(c)
        else:
            
            for i in range(1,k+1):
                if sum(c) + i <= n:
                    s.append(c+[i])
                
    return r[::-1]
