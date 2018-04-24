def deleteFromBST(t, queries):

    def max_hive(t):

        if t is None: return(None)
        while t.right is not None:
            t = t.right

        return(t.value)

    def noright(t):

        if t.right is None:
            return(t.left)
        else:
            t.right = noright(t.right)
            
        return(t)

    def bst(t, q):
        if t is None: return(None)
        if q == t.value:
            if t.left:
                t.value = max_hive(t.left)
                t.left = noright(t.left)
            else:
                t = t.right
        elif q < t.value:
            t.left = bst(t.left, q)
        elif q > t.value:
            t.right = bst(t.right, q)
        return(t)

    for q in queries:
        t = bst(t, q)

    return(t)
