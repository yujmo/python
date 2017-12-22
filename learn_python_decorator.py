import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("%s %s()" % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print("2017-12-23")
#now=log('execute')(now)
now()
print(now.__name__)

#重点：
#    首先执行log('execute')，返回的是decorator函数，再调用返回的函数，
#    参数是now函数，返回值最终是wrapper函数。




