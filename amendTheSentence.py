def amendTheSentence(s):
    words = []
    cword = ''
    for symb in s:
        if 64 < ord(symb) < 91:
            words.append(cword)
            cword = symb
        else:
            cword += symb
    words.append(cword)
    if '' in words:
        words.remove('')
    
    sent = ""
    for i in range(len(words)):
        cword = words[i]
        cword += ' '
        cword = smaller(cword)
        sent += cword
    
    return sent[:-1]

def smaller(word):
    firstChar = word[0]
    if 96 < ord(firstChar) < 123:
        return word
    firstChar = chr(ord(firstChar)+32)
    return firstChar + word[1:]
