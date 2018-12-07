"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        for i in range(len(nums)):

            dp[i] = nums[i]
        print(dp)
        


if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,1,0,1,99]
    res = s.singleNumber(nums)
    print(res)
    