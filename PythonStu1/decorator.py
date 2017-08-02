#Author:wanwang
import  time
# 简单的装饰器

def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("运行时间%s" % (stop_time - start_time))
    return deco

@timer   # foo1 = timer(foo1)
def foo1():
    time.sleep(1)
    print("in the foo1")
@timer
def foo2(name ,age):
    time.sleep(2)
    print("in the foo2 name is %s age is %s" % (name,age))
# def foo3():
#     time.sleep(2)
#     print("in the foo")
#     return "return func"
foo1()
foo2("ww","23")