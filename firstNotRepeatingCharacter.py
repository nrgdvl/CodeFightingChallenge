def firstNotRepeatingCharacter(s):
    
    indexed = {}
    twin_array = {}
    
    for i in range(len(s)):
        
        log = s[i]
        
        if log in twin_array:
            twin_array[log] += 1
        else:
            twin_array[log] = 1
            
        if log not in indexed:
            indexed[log] = i


    exception = [k for (k,v) in twin_array.items() if v == 1]
    if len(exception) < 1:
        return '_'
    
    indexed = dict([(k,v) for (k,v) in indexed.items() if k in exception])
    logged = min(indexed, key= indexed.get)
    
    return logged
