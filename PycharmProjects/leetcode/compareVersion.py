"""
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。
"""
class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l_version1 = version1.split(".")
        l_version2 = version2.split(".")
        tf_version1 = self.tfInt(l_version1)
        tf_version2 = self.tfInt(l_version2)
        if len(l_version1) == len(l_version2):
            if tf_version1 > tf_version2:
                return 1
            elif tf_version1 < tf_version2:
                return -1
            else: return 0
        elif len(l_version1) > len(l_version2):
            tf_version2 = tf_version2 * (10 ** (len(l_version1) - len(l_version2)))
            if tf_version1 > tf_version2:
                return 1
            elif tf_version1 < tf_version2:
                return -1
            else: return 0
        else:
            tf_version1 = tf_version1 * (10 ** ((len(l_version2) - len(l_version1))))
            if tf_version1 > tf_version2:
                return 1
            elif tf_version1 < tf_version2:
                return -1
            else: return 0
        
    def tfInt(self,version):
        """
        :parameter list version:
        :return: 转换后的int值
        """
        #tf_version = version.split(".")
        version.reverse()
        renum = 0
        for i in range(len(version)):
            renum += int(version[i]) * (10 ** i)
        return renum

if __name__ == '__main__':
    re = Solution()
    res = re.compareVersion('01','1')
    print(res)
        