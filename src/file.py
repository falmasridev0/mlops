import time
def timelimit(limit:int):

    def time_it(func):
        def wrapper(*args,**kwargs):
            t1 = time.time()
            result = func(*args,**kwargs)
            time.sleep(1)
            t2 = time.time()
            if t2-t1 > limit:
                print("alert! function exceeds time!")
            print(f"total_time: {t2-t1}")
            return result
        return wrapper
    return time_it
@timelimit(2)
def uppercase(text):
    return text.upper()
print(uppercase("hello"))