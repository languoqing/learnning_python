class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        l = [[] for i in range(len(A[0]))]
        for i in range(len(A[0])):
            for a in range(len(A)):
                l[i].append(A[a][i])
        return l

if __name__ == '__main__':
    a = Solution()
    l = [[5],[8]]
    res = a.transpose(l)
    print(res)