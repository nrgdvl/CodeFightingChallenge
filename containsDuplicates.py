def containsDuplicates(a):
    
    s = set()
    for i in a:
        if i in s:
            return True
        s.add(i)
    return False
