"""
给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
"""
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rflag = 0
        lflag = len(s) - 1
        flag = False
        for i in range(len(s)):
            if i == 0 and s[i] == ")":
                flag = False
            elif s[i] == "(":
                for a in range(rflag,len(s)):
                    if i < a and (s[a] == ")" or s[a] == "*"):
                        flag = True
                        rflag = a + 1
                        break
                    else: flag = False
        for n in range(len(s)-1,-1,-1):
            if n == len(s) - 1 and s[n] == "(":
                flag = False
            elif s[n] == ")":
                for b in range(lflag,-1,-1):
                    if n > b and (s[b] == "(" or s[b] == "*"):
                        flag = True
                        lflag = b-1
                        break
                    else: flag = False
                
        return flag

                
            
        
        

if __name__ == '__main__':
    s = Solution()
    st = "(*)))"
    res = s.checkValidString(st)
    print(res)
                