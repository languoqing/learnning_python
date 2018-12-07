"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        if len(s) < k:
            res = s[::-1]
        elif len(s) < 2 * k  and len(s) >= k:
            t_str = s[:k]
            re_str = t_str[::-1]
            res = re_str + s[len(re_str):]
        else:
            a = len(s) // (2*k)
            b = len(s) % (2*k)
            tem = 0
            for i in range(1,a+1):
                temstr = s[tem:2*k*i ]
                tem = 2 * k *i + 1
                n_str = temstr[0:k]
                rev_str = n_str[::-1]
                new_str = rev_str + temstr[len(temstr)-k:]
                res += new_str
            if b < k:
                t_str = s[2*k*a + 1:]
                res += t_str[::-1]
            if b < 2 * k and b >= k:
                t_str = s[2*k*a :]
                a_str = t_str[:k]
                re_str = a_str[::-1]
                print(re_str)
                res += re_str + t_str[len(re_str):]
        return res

if __name__ == '__main__':
    a = Solution()
    stra = "abcdefg"
    res = a.reverseStr(stra,1)
    print(res)

                
                
                
            