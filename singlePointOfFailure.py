def singlePointOfFailure(connections):    
    nodes = len(connections)
    timer = 0  
    less = [float("Inf")] * nodes  
    ids = [float("Inf")] * nodes 
    check_visit = [False] * nodes 
    connector = 0

    def microsys(current, parent = None):
        nonlocal timer, connector
        if not check_visit[current]:
            check_visit[current] = True
            less[current] = timer  
            ids[current] = timer  
            timer += 1
 
            for sibling, check in enumerate(connections[current]):
                if sibling == parent or not check: 
                    continue
                if not check_visit[sibling]:
                    microsys(sibling, current)
                    less[current] = min(less[sibling], less[current]) 
                    if less[sibling] > ids[current]:  
                        connector += 1
                else:
                    less[current] = min(less[current], ids[sibling])  

    for i in range(nodes):
        microsys(i)

    return connector  
