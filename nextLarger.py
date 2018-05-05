def nextLarger(a):

    checked = []
    twin_table = []

    for i in reversed(a):

        if not checked:
            twin_table = [-1] + twin_table
        else:
            for c in checked:

                if c > i:
                    twin_table = [c] + twin_table
                    break
            else:
                twin_table = [-1] + twin_table

        if i in checked: checked.rm(i)
        checked = [i] + checked

    return(twin_table)
