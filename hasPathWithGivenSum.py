def hasPathWithGivenSum(t, s):

    if t is None:
        if s == 0:
            return 1
        else:
            return 0
    else:
        result = 0
        twin_sum = s - t.value
        
        #рекурсия по ответвлениям 
        if t.left is not None:
            result = result or hasPathWithGivenSum(t.left, twin_sum)

        if t.right is not None:
            result = result or hasPathWithGivenSum(t.right, twin_sum)

        if twin_sum == 0 and t.left == None and t.right == None :
                return 1      
                  
        return result
