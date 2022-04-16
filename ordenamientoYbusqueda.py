def binarysearch(array, arg):
    array.sort()
    ini = 0; fin = len(array)-1
    while ini <= fin:
        pos = (ini + fin)/2
        if arg == array[pos]:
            return pos
        elif arg < array[pos]:
            fin = pos-1
        else:
            ini = pos+1
    return None


def mergesort(): 
    return None
