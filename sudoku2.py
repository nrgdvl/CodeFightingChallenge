def validrow(row):
    
    twinDictionary = {}    
    valid = True
    
    if len(row) > 0:

        #вывести если valid
        for r in row:
            if r in twinDictionary:
                twinDictionary[r] += 1
            else:
                twinDictionary[r] = 1
        
        #невалидный
        if twinDictionary[max(twinDictionary, key=twinDictionary.get)] > 1:
            valid = False
    
    return valid
                

def validblock(block):
    
    valid = True
    
    for i in range(len(block)):       
        row = [int(x) for x in block[i] if x != '.']
        valid = validrow(row)
        if not valid:
            break
                
    return valid

def sudoku2(block):
    
    result = False
     
    validrows = validblock(block) 
    col_valid = validblock(list(zip(*block)))
           
    block3x3_valid = True
    for i in range(0,len(block), 3):
        
        if not block3x3_valid:
                break
                
        compilate = block[i:i+3]
        
        for j in range(0,len(block[0]),3):
            
            twinList = [x[j:j+3] for x in compilate] 
            twinList = [twinList[k][l] for k in range(len(twinList)) for l in range(len(twinList[k]))]
            
            row = [int(x) for x in twinList if x != '.']
            block3x3_valid = validrow(row)  
            if not block3x3_valid:
                break
        
            
    if validrows and col_valid and block3x3_valid:
        result = True
        
    return result
