def firstDuplicate(a):

    matching = 0
    twin_array = {}

    for i in range(len(a)):
        if a[i] in twin_array:
            twin_array[a[i]] += 1
        else:
            twin_array[a[i]] = 1

        if(twin_array[a[i]] == 2):
            return a[i]

    if not matching:
        return -1