def countClouds(skyMap):
    
    amount = 0 
    if not skyMap:
        return amount
 
    rows = len(skyMap)
    blocks = len(skyMap[0])
    flags = []
    
    def getCloud():
        while flags:
            x,y = flags.pop(0)
            skyMap[x][y] = 'X'
            # check all four borders
            if x+1 < rows and skyMap[x+1][y] == '1':
                flags.append((x+1,y))
            if x-1 >= 0 and skyMap[x-1][y] == '1':
                flags.append((x-1,y))
            if y+1 < blocks and skyMap[x][y+1] == '1':
                flags.append((x,y+1))
            if y-1 >= 0 and skyMap[x][y-1] == '1':
                flags.append((x,y-1))
    
    for x in range(rows):
        for y in range(blocks):
            if skyMap[x][y] == '1':
                amount+=1
                flags.append((x,y))
                getCloud()
    
    return amount
