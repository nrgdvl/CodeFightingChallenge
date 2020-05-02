def longestPath(fileSystem):
    
    limit = 0
    path = {0: 0}
    
    for file in fileSystem.split("\f"):
        longlines = file.count('\t')
        label = len(file) - longlines
        if '.' in file: 
            limit = max(limit, path[longlines] + label)
        else: 
            path[longlines+1] = path[longlines] + label + 1
    return limit
