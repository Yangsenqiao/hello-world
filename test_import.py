def my_abs(x):
    if x>0:
        return x
    else:
        return -x
def calc(*numbers):#只需要在形参前面加一个*就可以变长了
    sum=1
    for i in numbers:
        sum=sum*i
    return sum
def jie(x):
    if x==1:
        return x
    else:
        return x*jie(x-1)

#def add(形参，形参，xxx="")最后一个是默认参数，就是如果你传参的时候没有这个，那就用默认参数，反之使用传进来的
#使用默认参数的好处就在于，比如统计学生的信息时候，只需要外省的人传一下地理位置这个参数，其他人不用
if __name__=="__main__":#这么写是为了执行脚本时候，这个main函数才会执行，而如果直接import到了其他函数则不会执行

    print(my_abs(230))
    print(calc(1,3,5))
    print(jie(10))


