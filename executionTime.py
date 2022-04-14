from datetime import timedelta, datetime


def howlong(func, *args, **kwargs):
    """this function calculate execution time of a function"""
    star = datetime.now()
    originReturn = func(*args, **kwargs)
    end = datetime.now()
    delta = (end - star)/timedelta(milliseconds=1)
    print('Execution time is: ', round(delta, 4))
    return originReturn


def decorator(func):
    """use how @decorator for it calculate execution time of a function"""
    def aux(*args, **kwargs):
        star = datetime.now()
        originReturn = func(*args, **kwargs)
        end = datetime.now()
        delta = (end - star)/timedelta(milliseconds=1)
        print('Execution time is: ', round(delta, 4))
        return originReturn
    return aux


#probar directamente con time()
#cambiar ubicación y subir a git
