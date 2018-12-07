"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = {}
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        else:
            r[0] = nums[0]
            r[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):
                r[i] = max(r[i-1],r[i-2]+nums[i])
        print(r)
        return r[len(nums)-1]
        
if __name__ == '__main__':
    a = Solution()
    nums = [3,4,7,29,9]
    res = a.rob(nums)
    print(res)