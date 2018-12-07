'''
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        relist = [0]
        slist = path.split('/')
        repath = ""
        for i in slist:
            if i == "..":
                if relist:
                    relist.pop()
            elif i == '' or i == ".":
                continue
            else: relist.append(i)
        if relist:
            for y in relist:
                repath += "/{}".format(y)
            return repath
        else: return '/'
    
if __name__ == '__main__':
    s = Solution()
    re = s.simplifyPath("/")
    print(re)