#-*- coding:utf-8 -*-
"""有1000只水桶，其中有且只有一桶装的含有毒药，其余装的都是水。它们从外观看起来都一样。如果小猪喝了毒药，它会在15分钟内死去。

问题来了，如果需要你在一小时内，弄清楚哪只水桶含有毒药，你最少需要多少只猪？

假设有 n 只水桶，猪饮水中毒后会在 m 分钟内死亡，你需要多少猪（x）就能在 p 分钟内找出“有毒”水桶？n只水桶里有且仅有一只有毒的桶。
"""

import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        if buckets == 1:
            return 0
        else:
            cantestbukets = math.ceil(minutesToTest / minutesToDie) + 1
            return self.pow_n(int(cantestbukets), buckets)
    
    def pow_n(self, n, num):
        num = math.ceil(num / n)
        count = 0
        while num > 0:
            print(num)
            count += 1
            if num == 1:
                break
            num = math.ceil(num / n)
        return count
    
if __name__ == '__main__':
    a = Solution()
    re = a.poorPigs(4,1,2)
    print(re)