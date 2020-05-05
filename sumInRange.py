
def sumInRange(nums, queries):

    sumation=0
    lst=[]
    for i in range(len(queries)):  
        lst=nums[queries[i][0]:queries[i][1]+1]
        sumation += sum(lst)
    return int(sumation%(1000000000+7))
def sumInRange(nums, queries):
    dic = {}
    su = 0
    for i, e in enumerate(nums):
        su += e
        dic["0_{}".format(i)] = su
    sum_r = 0
    for i in queries:
        a, b  = i
        if '{}_{}'.format(a,b) in dic:
            sum_r += dic['{}_{}'.format(a,b)]
        else:
            t = dic['0_{}'.format(b)] - dic['0_{}'.format(a-1)]
            dic['{}_{}'.format(a,b)] = t
            sum_r += t
    return sum_r % 1000000007
