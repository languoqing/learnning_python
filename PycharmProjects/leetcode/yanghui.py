#-*- coding:utf-8 -*-
"""
    [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #控制总层数
        for i in range(numRows):
            #控制列表长度
            for b in range(i):
                if b == 0 or b == i - 1: