def reverseNodesInKGroups(l, k):

    def reverso(x):
        twin_array = []
        while x is not None:
            twin_array.append(x.value)
            x = x.next
        return(twin_array)

    list_l = reverso(l)

    twin_array = []
    for start in range(0, len(list_l), k):
        end = start + k
        sublist = list_l[start:end]

        #тогда срез 
        if len(sublist) < k:
            twin_array += sublist[:]
        else:
            twin_array += sublist[::-1]

    return(twin_array)
