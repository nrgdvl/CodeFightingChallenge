def findProfession(level, pos):
    if level == 1:
        return 'Engineer'
    if level == 2:
        if pos == 1:
            return 'Engineer'
        else:
            return 'Doctor'
    if pos % 2 == 1:
        return findProfession(level - 1, (pos+1)/2)
    else:
        if findProfession(level - 1, pos/2) == 'Doctor':
            return 'Engineer'
        else:
            return 'Doctor'
