#-*- coding:utf-8 -*-
"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，
则返回  -1。
"""
def strStr(Astr,Bstr):
    '''Astr 需要包含Bstr，不存在返回-1'''
    if Astr == Bstr:
        return 1
    elif Astr == '' or  Bstr == '':
        return -1
    elif (Astr and Bstr) or (Astr != '' and Bstr != ''):
        for i in range(len(Astr)-1):
            if Astr[i:i + len(Bstr)] == Bstr:
                return 1
        return -1
    return 0
        
    

if __name__ == '__main__':
    a = strStr('a','a')
    print(a)