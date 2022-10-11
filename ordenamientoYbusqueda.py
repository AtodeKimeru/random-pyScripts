import random


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


def mergesort(lista): 
    if len(lista) > 1:
        middle = len(lista)  // 2
        left = lista[:middle]
        right = lista[middle:]

        print(left, '*' * 5, right)

        # recursion
        mergesort(left)
        mergesort(right)

        # iterators
        i = 0
        j = 0
        k = 0 # main list

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            lista[k] =  left[i]
            i += 1
            k += 1

        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

        print(f'izquierda {left}, derecha {right}')
        print(lista)
        print('-' * 50)

    return lista


def run():
    list_length = int(input('What will be list length?'))

    lista = [random.randint(0, 100) for i in range(list_length)]
    print(lista)
    print('-' * 20)

    sortlista = mergesort(lista)
    print(sortlista)


if __name__ == '__main__':
    run()