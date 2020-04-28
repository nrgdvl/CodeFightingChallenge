def nearestGreater(a):
    # get b.len
    b = [0] * len(a)
    buffer = []
    
    for i in range(len(a)):
        
        while buffer and a[buffer[-1]] < a[i]:
            next_i = buffer.pop()
            if b[next_i] == -1 or i - next_i < next_i - b[next_i]: 
                b[next_i] = i
        if not buffer:
            b[i] = -1
        else: 
            if a[buffer[-1]] > a[i]:
                b[i] = buffer[-1]
            else: 
                b[i] = b[buffer[-1]]
        buffer.append(i)
    return b
