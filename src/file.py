"""
Module docstring
"""
import time

def timelimit(limit:int):
    """
    Docstring for timelimit
    
    :param limit: Description
    :type limit: int
    """
    def time_it(func):
        """
        Docstring for time_it
        
        :param func: Description
        """
        def wrapper(*args,**kwargs):
            """
            Docstring for wrapper
            
            :param args: Description
            :param kwargs: Description
            """
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
    """
    Docstring for uppercase
    
    :param text: Description
    """
    return text.upper()


print(uppercase("hello"))

def new_dummy_fun():
    """
    Docstring for new_dummy_fun
    """
    print("hello")
