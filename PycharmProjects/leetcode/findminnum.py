'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数
'''
def findMinNum(l):
    if l == []:
        return 1
    sortlist = sorted(l)
    zlist = []
    for x in sortlist:
        if x > 0 and x not in zlist:
            zlist.append(x)
    if zlist == []:
        return 1
    flag = 0
    for x in range(len(zlist)):
        if zlist[x] == zlist[0] + x: #判断是否为连续数组
            flag = 1
        else: flag = 2
    if zlist[0] != 1:
        return 1
    else:
        if flag == 1:
            return zlist[-1] + 1
        else:
            for x in range(len(zlist)):
                if zlist[x] != zlist[0] + x:
                    return zlist[x-1] + 1
    
# def reNumSelect(sorted_list):
#     '''re : flag:1,连续，2，非连续'''
#     flag = 0
#     for x in range(len(sorted_list)):
#         if sorted_list[x] == sorted_list[0] + x:
#             flag = 1
#         else: flag = 2
#     return flag
#
        
        
    
        

if __name__ == '__main__':
    ll = [0,1,1,2,2]
    res = findMinNum(ll)
    print(res)

    
    