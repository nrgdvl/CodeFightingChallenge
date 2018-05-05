from string import ascii_lowercase as letters

digits = '1234567890'

def decodeString(s):

    buffer = []
    string = [x for x in s]

    def cumputer(chars, mult = 1):
        if buffer:
            tmp = buffer.pop()
        else:
            tmp = ''
        if tmp == ']': tmp = ''
        buffer.append(mult * chars + tmp)

    while string:
        if string[-1] == '[':
            string.pop()
            continue

        if string[-1] == ']':
            buffer.append(string.pop())
            continue

        if string[-1] in letters:
            cumputer(string.pop())
            continue

        if string[-1] in digits:
            mult = string.pop()

            if string:
                while string[-1] in digits:
                    mult = string.pop() + mult
                    if not string: break
                    
            cumputer(buffer.pop(), int(mult))
            continue

    return(''.join(buffer))
