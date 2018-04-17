def addTwoHugeNumbers(a, b):
    
    twin_a = a
    twin_b = b

    #словарь даст ошибку 
    a_string = ""
    b_string = ""
    
    while twin_a:
        a_string += esliNoZero(twin_a.value)
        twin_a = twin_a.next
        
    while twin_b:
        b_string += esliNoZero(twin_b.value)
        twin_b = twin_b.next
    
    ostatok = int(a_string) + int(b_string)

    result = []
    strresult = str(ostatok) 
    
    i = len(strresult)-1
    j = 1
    result = []
    final_result = []
    
    while i >= 0:
        final_result.insert(0,strresult[i])
        if j==4:
            result.insert(0,final_result)
            final_result = []
            j=0
        j+=1
        i -= 1
        
    if len(final_result):
        result.insert(0,final_result) 
    result2 = []
    
    for i in result:
        z = ""
        for e in i:
            z += e
        result2.append(int(z))
                
    return result2

def esliNoZero(beZero):
    beZero = str(beZero)
    
    if len(beZero) == 1:
        return "000" + beZero

    #если больше позиций с нулями     
    elif len(beZero) == 2:
        return "00" + beZero
    elif len(beZero) == 3:
        return "0" + beZero
    else:
        return beZero
