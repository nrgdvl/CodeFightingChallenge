def feedingTime(classes):
    
    nodes = len(classes)
    colors = [0] * nodes
    
    gra = [[0 for _ in range(nodes)] for _ in range(nodes)]  
    classes = [set(c) for c in classes]
    
    for i in range(nodes-1):
        for j in range(i+1, nodes):
            if classes[i].intersection(classes[j]):
                gra[i][j] = 1
                gra[j][i] = 1
    
    def colorable(current, colors, color):
        for sibling in range(nodes):
            if gra[current][sibling] == 1 and colors[sibling] == color:
                return False 
        return True
    
    def gracolor(current, k):
        if current == nodes:
            return True  
        
        for color in range(1, k+1): 
            if colorable(current, colors, color):
                colors[current] = color
                
                if gracolor(current+1, k):
                    return True 
                
                colors[current] = 0
    
        return False  
        
    for k in range (1, 6):
        if gracolor(0, k):
            return k  
    
    return -1
