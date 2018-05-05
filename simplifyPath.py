def simplifyPath(path):

    array = path.split('/')
    result = []
    
    for e in array:
        if e == '' or e == '.':
            pass
        elif e == '..':
            if len(result) > 0:
                result.pop()
        else:
            result.append(e)
    if len(result) == 0:
        return '/'

    return "/"+'/'.join(result)
