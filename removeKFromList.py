def removeKFromList(l, k):
    
    #если совпадений нет  
    while l and l.value == k:
        l = l.next

    twin_larray_sorted = l
    #если есть 
    while twin_larray_sorted: 
        reversoCheck_array = twin_larray_sorted
        twin_larray_sorted = twin_larray_sorted.next
        while twin_larray_sorted and (twin_larray_sorted.value == k):
            twin_larray_sorted = twin_larray_sorted.next
        reversoCheck_array.next = twin_larray_sorted 
    return l

    #если запихают пустой массив 
    if l is None:
        return []
