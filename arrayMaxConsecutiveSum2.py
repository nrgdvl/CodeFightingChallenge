def arrayMaxConsecutiveSum2(inputArray):

    dist = inputArray[0]
    lim = 0

    for full in inputArray:
        lim += full 

        if lim<full:
            lim=full

        if lim > dist:
            dist = lim
    return( dist)
