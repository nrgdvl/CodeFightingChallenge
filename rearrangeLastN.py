def rearrangeLastN(l, n):

    #буферный массив
    def converter(x):
        twin_array = []
        while x is not None:
            twin_array.append(x.value)
            x = x.next
        return(twin_array)

    list_l = converter(l)

    return(list_l[-n:]+list_l[:-n])
