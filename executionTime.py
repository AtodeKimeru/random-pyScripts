import time


def exTime(func):
    """use how @decorator for it calculate execution time of a function"""
    def aux(*args, **kwargs):
        star = time.time()
        originReturn = func(*args, **kwargs)
        end = time.time()
        delta = (end - star)*1000 #in milliseconds
        print('Execution time is: ', round(delta, 4))
        return originReturn
    return aux


def duration(func, *args, **kwargs):
    """this function calculate execution time of a function 'func'"""
    star = time.time()
    originReturn = func(*args, **kwargs)
    end = time.time()
    delta = (end - star)*1000 #in milliseconds
    print('Execution time is: ', round(delta, 4))
    return originReturn
