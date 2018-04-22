def groupingDishes(dishes):

    twin_dictionary = {}

    for dish in dishes:
        basic = dish[0]
        dish = dish[1:]

        #сопоставление 
        for i, v in enumerate(dish):
            if v in twin_dictionary:
                twin_dictionary[v] = twin_dictionary[v] + [basic]
            else:
                twin_dictionary[v] = [basic]
    #фильтр
    filtred_resultay = {}
    for k, v in twin_dictionary.items():
        if len(v) > 1:
            filtred_resultay[k] = v

    new = sorted(filtred_resultay.items())
    
    result = []
    for i in new:
        result.append([i[0],*sorted(i[1])])
    
    return result
