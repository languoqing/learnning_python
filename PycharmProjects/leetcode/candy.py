"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
"""
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candylist = [1]
        #print("ratings {}".format(ratings))
        for x in range(1,len(ratings)):
            if ratings[x] > ratings[x-1]:
                candylist.append(candylist[x-1] + 1)
            else:
                if ratings[x] < ratings[x-1] and x == 1:
                    candylist.append(1)
                    candylist[x-1] = candylist[x] + 1
                else: candylist.append(1)
        #print("canylist 1 {}".format(candylist))
        for y in range(len(ratings)-1,0,-1):
            if ratings[y] > ratings[y-1]:
                if candylist[y] > candylist[y-1]:
                    continue
                else: candylist[y-1] = candylist[y] + 1
            elif ratings[y] < ratings[y-1]:
                if candylist[y] < candylist[y-1]:
                    continue
                else: candylist[y-1] = candylist[y] + 1
            else:
                if candylist[y] >= candylist[y-1]:
                    continue
                else: candylist[y-1] = candylist[y] + 1
        #print("candylist 2 {}".format(candylist))
        res_sum = 0
        for s in candylist:
            res_sum += s
        return res_sum
    
if __name__ == '__main__':
    re = Solution()
    l = [1,3,4,5,2]
    res = re.candy(l)
    print(res)
        
        
        
        
        