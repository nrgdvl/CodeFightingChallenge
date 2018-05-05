def minimumOnStack(operations):

    height = 0
    buffer = []

    limit = [None]
    border = [float('Inf')]

    result = []

    for i in operations:
        i = i.split(' ')

        if i[0] == 'min':
            result.append(border[-1])
            continue

        if i[0] == 'push':
            val = int(i[1])
            buffer.append(val)
            height += 1
            if val < border[-1]:
                limit.append(1)
                border.append(val)
            elif val == border:
                limit[-1] += 1
            continue

        if i[0] == 'pop':
            val = buffer.pop()
            height -= 1
            if val == border[-1]:
                limit[-1] -= 1
                if not limit[-1]:
                    border.pop()
                    limit.pop()
            continue

    return(result)

if __name__ == '__main__':
    operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop",
                  "min", "pop", "min"]
    print(minimumOnStack(operations))
