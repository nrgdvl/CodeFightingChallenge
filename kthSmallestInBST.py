def kthSmallestInBST(t, k):

    memory = []
    rate = []

    while(len(rate) < k):
        while t is not None:
            memory.append(t)
            t = t.left
        top = memory.pop()
        rate.append(top.value)
        t = top.right

    return(rate[-1])
