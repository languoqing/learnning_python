'''
给定一个整数数组 A，以及一个整数 target 作为目标值，返回满足 i < j < k 且 A[i] + A[j] + A[k] == target 的元组 i, j, k 的数量。
由于结果会非常大，请返回 结果除以 10^9 + 7 的余数。

示例 1：
输入：A = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举（A[i]，A[j]，A[k]）：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
示例 2：
输入：A = [1,1,2,2,2,2], target = 5
输出：12
解释：
A[i] = 1，A[j] = A[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
提示：
3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
'''
def findnum(num,lis):
    '''return True,False'''
    for i in range(len(lis)):
        if num == lis[i]:
            return i

def countThreeSum(lis,target):
    count = 0
    lis.sort()
    print(lis)
    for i in range(len(lis)):
        for y in range(len(lis) - 1 ):
            if  lis[y] >= lis[i]:
                thenum = target - (lis[y] + lis[i])
                if findnum(thenum,lis) and thenum >= lis[y]:
                    count += 1
                    print('list[{}]={},list[{}]={},list[{}]={}'.format(i,lis[i],y,lis[y],findnum(thenum,lis),thenum))
    return count
            
if __name__ == '__main__':
    lis1 = [1,2,3,2,3,4,2,8]
    target = 9
    res = countThreeSum(lis1,target)
    print('res+++++++:{}'.format(res))
    