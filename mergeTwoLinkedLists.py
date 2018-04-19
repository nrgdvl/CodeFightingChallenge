def mergeTwoLinkedLists(l1, l2):
    returnable = []
    
    while l1 and l2:
        if l1 and l2 and l1.value < l2.value:

            returnable.append(l1.value)
            l1 = l1.next

        if l1 and l2 and l2.value < l1.value:
            returnable.append(l2.value)
            l2 = l2.next

        if l1 and l2 and l1.value == l2.value:

            returnable.append(l1.value)
            returnable.append(l2.value)

            l1 = l1.next
            l2 = l2.next

        if  l1 and l2 is None:
            returnable.append(l1.value)
            l1 = l1.next

        if  l2  and l1 is None:
            returnable.append(l2.value)
            l2 = l2.next

    #hidden даёт не зачёт
    if l1 is None:

        while l2:
            returnable.append(l2.value)
            l2 = l2.next 

    if l2 is None:

        while l1:
            returnable.append(l1.value)
            l1 = l1.next 
    
    return returnable
