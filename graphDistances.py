def graphDistances(g, s):
    le = len(g)
    for i in range(le):
        for y in range(le):
            if g[i][y] == -1:
                g[i][y] = float('inf')
                
    for w in range(le):
        for x in range(le):
            for j in range(le):
                g[x][j] = min(g[x][j], g[x][w] + g[w][j])
    
    g[s][s] = 0 
    return g[s][:]
