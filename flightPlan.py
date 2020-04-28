def flightPlan(time, source, destination):
    
    def min_convert(t):
        t = t.split(':')
        hours = t[0]
        minutes = t[1]
        return int(hours) * 60 + int(minutes)
    
    path = {}
    path[source] = -60 
    k = float("inf")
    
    time = sorted(time, key=lambda a: a[-2]) 
    
    for location, l_array, dtime, arr_time in time:
        if path.get(location, k) + 60 <= min_convert(dtime): 
            path[l_array] = min(path.get(l_array, k), min_convert(arr_time))
    
    def convertBack(t):
        h, t = divmod(t, 60)
        return "{:02}:{:02}".format(h, t)
    
    if path.get(destination):
        return convertBack(path[destination])
    else:
        return "-1"
