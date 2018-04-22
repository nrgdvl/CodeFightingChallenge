def possibleSums(coins, quantity):

    summs = set([0])

    for capacity, number in zip(coins, quantity):

        new_summs = set([0])
        
        for q in range(number + 1):
            for base in summs:
                new_summs.add(base + q * capacity)
        summs = new_summs

    summs.remove(0)

    return(len(summs))
