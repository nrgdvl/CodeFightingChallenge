def digitTreeSum(t):

    tmp = [[0,t]]
    tmp_2 = []
    while tmp:
        pop1,pop2 = tmp.pop(0)
        if pop2.left:
            tmp.append([pop1*10+pop2.value,pop2.left])
        if pop2.right:
            tmp.append([pop1*10+pop2.value,pop2.right])
        if not pop2.left and not pop2.right:
            tmp_2.append(pop1*10+pop2.value)
    
    return sum(tmp_2)
