#Author:wanwang
import  time
# 简单的装饰器
def log():
    print("当前时间 %s"% time.asctime(time.localtime(time.time())))
def deco(func):
    def wrapper(*args,**kwargs):
        log()
        return func(*args,**kwargs)
    return wrapper
@deco #foo = deco()
def foo(name = "ww"):
    print("this is foo ande name %s"% name)
@deco
def bar():
    print("this is bar")
@deco
def test(name = "ww"):
    return name
foo()
bar()
test()