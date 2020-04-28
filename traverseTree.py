def traverseTree(t):
    
    u = t
    src = [u]
    result = []
    if not t:
        return []
    while len(src):
        x = src.pop(0)
        result.append(x.value) 
        if x.left:
            src.append(x.left)
        if x.right:
            src.append(x.right)   
            
    return result
