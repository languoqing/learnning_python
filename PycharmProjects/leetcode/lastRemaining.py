"""
给定一个从1 到 n 排序的整数列表。
首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。
第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。
我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
返回长度为 n 的列表中，最后剩下的数字。
"""
class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        int_list = [a for a in range(1,n+1)]
        copy_list = int_list[:]
        flag = 1
        count = 1
        while flag:
            if len(int_list) == 1:
                flag = 0
            elif count % 2 == 1:
                for i in range(len(copy_list)):
                    if i % 2 == 0:
                        int_list.remove(copy_list[i])
                count += 1
                copy_list = int_list[:]
                #print("copy_List 1 {} count{}".format(copy_list,count))
            else:
                for a in range(len(copy_list)-1,-1,-1):
                    if len(copy_list) % 2 == 1:
                        if a % 2 == 0:
                            int_list.remove(copy_list[a])
                    else:
                        if a % 2 == 1:
                            int_list.remove(copy_list[a])
                count += 1
                copy_list = int_list[:]
                #print("copy_list2 {} count{}".format(copy_list,count))
            
        return int_list[0]
        
        

if __name__ == '__main__':
    obj = Solution()
    res = obj.lastRemaining(1200)
    print(res)
        
        