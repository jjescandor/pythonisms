from functools import wraps

def Error(func):
    def Function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__}: wrong data type")
    return Function

@Error
def divide(int,l):
    print(int/l)



def proclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f"{orig_val.upper()}!!!"
    return wrapper

@proclaim
def say(txt):
    return txt

if __name__ == "__main__":
    print(say("tiktok is overrated"))
    divide('hello','world')