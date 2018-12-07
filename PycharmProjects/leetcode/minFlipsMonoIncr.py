'''
如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调递增的。
我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
返回使 S 单调递增的最小翻转次数。
'''
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        N = len(S)
        dp = [0] * 2
        for i in range(1, N + 1):
            if S[i - 1] == '0':
                dp[0] = dp[0]
                dp[1] = min(dp[1], dp[0]) + 1
            else:
                dp[1] = min(dp[1], dp[0])
                dp[0] = dp[0] + 1
        return min(dp[0], dp[1])


    
if __name__ == '__main__':
    a = Solution()
    lstr = "010001"
    res = a.minFlipsMonoIncr(lstr)
    print(res)
    
    
        
        
    