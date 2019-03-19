#-*- coding:utf-8 -*-
"""
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。

给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False
"""
# class Solution(object):
#     def checkPerfectNumber(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         temp = 0
#         for i in range(1,num):
#             if num % i == 0:
#                 temp += i
#         if num == temp:
#             return True
#         else: return False
import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<6:
            return False
        temp=num-1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                temp=temp-i-num/i
        if (int(math.sqrt(num))) ** 2==num:
            temp=temp+-int(math.sqrt(num))
        if temp==0:
            return True
        else:
            return False


if __name__ == '__main__':
    a = Solution()
    re = a.checkPerfectNumber(100000000)
    print(re)