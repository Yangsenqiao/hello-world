d={'YSQ':230,'WYF':'NB'}#只要使用一个花括号相当于声明一个字典，字典的优势在于可以查的快
print(d['WYF'])#记住，print时候要把那个当成一个列表
print('WYF'in d)#返回值True
d.pop('YSQ')#删除一个键值
print(d)


#set用于不重复的存储
s=set([1,2,3])#首先要传入一个list
print(s)#打印结果是：{1,2,3}
#通过s.add可以加入数值，通过s.remove来删除，而使用set一般用于做集合之间的交集并集补集

#使用hex()函数可以将一个整数转换为16进制
print(hex(12))
from test_import import my_abs#切记引用的时候不要加入.py
print(my_abs(-100))
#return函数可以返回多个值（虽然只是假象）本质上返回的是一个tuple元组
