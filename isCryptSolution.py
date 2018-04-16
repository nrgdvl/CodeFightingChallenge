def isCryptSolution(crypt, solution):
    solution  = dict((x[0],x[1]) for x in solution)
    twinArray = []
    flag = True
    for word in crypt:
        word = "".join(solution[i] for i in word if i in solution)
        twinArray.append(word)
        if word[0]=="0" and len(word)>1:
            flag = False
    twinArray = list(map(int,twinArray))
    if (twinArray[0] + twinArray[1])!=twinArray[2]:
        flag = False
    return flag
