'''
给定一个无序的整数数组，找到其中最长上升子序列的长度
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
'''

class Solution:
    def lengthOfLIS(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        if arr == []:
            return 0
        if len(arr) == 1:
            return 1
        lindex = [1]
        l = []
        rel = []
        for x in range(1,len(arr)):
            if arr[x] < arr[x-1]:
                lindex.append(x)
        for x in lindex:
            for y in range(x,len(arr)):
                if arr[y] > arr[y-1] and y == 1:
                    l.append(arr[y-1])
                elif arr[y] > arr[y-1]:
                    l.append(arr[y])
                elif arr[y] == arr [y-1] and arr[y] not in l:
                    l.append(arr[y])
                else:
                    arr[y] = arr[y-1]
            rel.append(len(l))
        return rel[-1]
        

     
 

        
        

        
    
if __name__ == '__main__':
    l = [10,9,2,5,3,7,101,18]
    a = Solution()
    res = a.lengthOfLIS(l)
    print(res)