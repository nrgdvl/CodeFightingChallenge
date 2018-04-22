def containsCloseNums(numbers, k):
    
    before = dict()
    
    for position, number in enumerate(numbers):
        
        try:
            if position - before[number] <= k: return (True)
        except:
            pass
        before[number] = position

    return (False)


if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 5, 2]
    k = 3
    print(containsCloseNums(numbers, k))
