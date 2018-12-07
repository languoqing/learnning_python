#-*- coding:utf-8 -*-
try:
    w = []
    with open(r"C:\Users\ex-languoqing600\Desktop\1.txt","r") as f:
         for i in f.readlines():
             a = i.split('、')
             #print(w)
             w = w + a
except Exception as e:
    print(e)
# print(w)

try:
    a = []
    with open(r"C:\Users\ex-languoqing600\Desktop\2.sql","r") as f:
        for i in f:
            b = i.split("'")
            a.append(b[1])
except Exception as e:
    print(e)

if __name__ == '__main__':
    print(len(w))
    s_w = set(w)
    s_a = set(a)
    #比较差集
    print(len(s_w))
    re = s_w - s_a
    print(re)
    print(len(re))

