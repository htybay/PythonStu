#Author:wanwang
import time

def log():
    print("当前时间 %s"% time.asctime(time.localtime(time.time())))
#带参数的装饰器
def use_log(flag):
    def deco(func):
        def wrapper(*args,**kwargs):
             if flag == "wan":
               log()
             return func(*args, **kwargs)
        return wrapper
    return deco
@use_log(flag="wan")
def foo():
    print("this is foo")
@use_log(flag ="wan")
def coumt(x):
    return x
@use_log(flag="ww")
def bar():
    print("this is bar")
print(coumt(3))
foo()
bar()