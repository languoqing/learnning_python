# a = [1,2,3,4,2,4,5]
# b = [5,4,3]
# # for i in a:
# #     print(i)
#
# for i in range(len(a)):
#     print(i)
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l = [[0]] * len(A)
# print(l[1])
# # for i in range(1,len(A)):
# #     for a in range(len(A)):
# #         l[i].append(A[a][i])

def a():
    return 5

def b(args):
    re = args()
    try:
        assert 4 == re
    except AssertionError as e:
        print("断言{}".format(e))
b(a)

            


            
    
    





    

