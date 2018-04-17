def isListPalindrome(l):

    twin_array = []
    i = 0
    while l:
        twin_array.append(l.value)
        l = l.next
    
    #переворот
    return(twin_array == twin_array[::-1])
