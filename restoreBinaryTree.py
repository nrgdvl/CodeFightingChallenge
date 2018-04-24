def restoreBinaryTree(inorder, preorder):

    initial = preorder[0]
    basic = Tree(initial)
    position = inorder.index(initial)

    left = inorder[:position]
    right = inorder[(1+position):]

    prevl = preorder[1:(position+1)]
    prevr = preorder[(1+position):]

    if left: basic.left  = restoreBinaryTree(left, prevl)
    if right: basic.right = restoreBinaryTree(right, prevr)

    return(basic)
