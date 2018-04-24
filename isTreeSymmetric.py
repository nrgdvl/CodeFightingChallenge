
    
def isTreeSymmetric(t):

    if t == None:
        return 1
    
    left_branch = None
    right_branch = None
     
    if t.left is not None:
        left_branch = t.left
         
    left_list = inOrderTraversal(left_branch)
    print(left_list)
     
    if t.right is not None:
        right_branch = t.right
         
    right_list = reversedInOrderTraversal(right_branch)
    print(right_list)
    
    if left_list == right_list:
        return 1
    else:
        return 0
    
def inOrderTraversal(t, list=[]):
    
    if t == None:
        return []

    if t.left is not None:
        inOrderTraversal(t.left,list)
    list += [t.value]
    
    if t.right is not None:
        inOrderTraversal(t.right,list)
    
    return list



def reversedInOrderTraversal(t, rlist=[]):
    
    if t == None:
        return []

    if t.right is not None:
        reversedInOrderTraversal(t.right)
    rlist += [t.value]
    
    if t.left is not None:
        reversedInOrderTraversal(t.left)
    
    return rlist
