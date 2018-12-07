'''
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
'''
def isLongPressName(name,Typed):
    a, b = countSingleWord(name)
    x, y = countSingleWord(Typed)
    if x >= a and b == y:
        return True
    else:
        return False

#>=2 ,且是连续的
def countSingleWord(name):
    count = 1
    l = []
    word1 = ''
    for i in range(len(name)):
        for y in range(len(name)):
            if name[y] == name[i] and y == i + 1:
                i = y
                count += 1
                word1 = name[y]
    return count,word1


    

if __name__ == '__main__':
    word = "leelee"
    ty = "lleeelee"
    s, x = countSingleWord(ty)
    a, b = countSingleWord(word)
    print(s,x)
    print(a,b)
    
    bol = isLongPressName(word,ty)
    print(bol)
    
    
                