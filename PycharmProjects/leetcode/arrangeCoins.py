"""
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内
"""
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = True
        count = 0
        a = 0
        tag = 0
        while flag:
            if tag + a >= n:
                flag = False
            else:
                a += 1
                tag += a
                # for i in range(a):
                #     print("*",end=" ")
                # print()
                count += 1
        return count

if __name__ == '__main__':
    a = Solution()
    n = 9
    res = a.arrangeCoins(n)
    print(res)