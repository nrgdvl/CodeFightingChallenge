def pressingButtons(buttons):
    walkthroug = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
              '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    combos = []
    for i in buttons:
        if not combos:
            for symb in walkthroug[i]:
                combos.append(symb)
        else:
            coombos = []
            for symb in walkthroug[i]:
                for word in combos:
                    coombos.append(word + symb)
            combos = coombos
    return sorted(combos)
