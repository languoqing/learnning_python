"""
设计一个算法，找出只含素因子2，3，5 的第 n 小的数。

符合条件的数如：1, 2, 3, 4, 5, 6, 8, 9, 10, 12...
思路：2的素因子隔2个，3的素因子隔3个，5的素因子隔4，一轮是2+3+4
"""
# def findSushu(n):
#     while True:
#         if n%7 > 0 :
#             cout1 += 1