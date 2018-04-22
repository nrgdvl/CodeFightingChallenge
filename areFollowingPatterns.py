def areFollowingPatterns(strings, patterns):

    input_tup = dict()
    twin_intup = dict()

    for i, (x, y) in enumerate(zip(strings, patterns)):
        
        try:
            p1 = input_tup[x]
        
        except:
            p1 = i
            input_tup[x] = i
        
        try:
            p2 = twin_intup[y]
        
        except:
            p2 = i
            twin_intup[y] = i
       
        if p1 != p2:
            return(False)

    return(True)
#исключения по примеру 
if __name__ == '__main__':
   
   strings= ["cat",
              "dog",
              "doggy"]
    patterns= ["a",
               "b",
               "b"]
               
    print(areFollowingPatterns(strings,patterns))
