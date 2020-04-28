def hasDeadlock(connections):   
    vis_or_not = [0] * len(connections)
    
    def checknode(node):
        if vis_or_not[node] == 0:
            vis_or_not[node] = 1
            for sibling in connections[node]: 
                #cycle if one
                if vis_or_not[sibling] == 1:
                    return True
                #check existance
                if checknode(sibling):
                    return True
            vis_or_not[node] = 2 

    for i in range(len(connections)):
        check = checknode(i)
        if check:
            return True
    return False
    
