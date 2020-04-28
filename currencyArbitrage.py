def currencyArbitrage(exchange):
    
    nodes = len(exchange) 
    
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                exchange[i][j] = max(exchange[i][j], exchange[i][k] * exchange[k][j])
    
    for i in range(nodes):
        if exchange[i][i] > 1: 
            return True
    return False
