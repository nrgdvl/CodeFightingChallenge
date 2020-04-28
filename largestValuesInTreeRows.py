def largestValuesInTreeRows(t):
    
    if not t:
        return []
    source = [[0,t]]
    result = []
    while source:
        i,x = source.pop(0)
        if len(result) <= i:
            result.append(x.value)
        else:
            result[i] = max(x.value,result[i])
        if x.left:
            source.append([i+1,x.left])        
        if x.right:
            source.append([i+1,x.right])
            
    return result
