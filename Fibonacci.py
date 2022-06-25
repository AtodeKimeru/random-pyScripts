def fibonacci(n: int) -> None:
    
    lastfibo = 0

    def recursive(N: int) -> int:
        if N == 2:
            print(1)
            return 1
        elif N > 2:
            nonlocal lastfibo
            recu = recursive(N-1)
            newfibo = recu + lastfibo
            lastfibo = recu
            print(newfibo)
            return newfibo


    if n < 1:
        print("the number isn't positive")
    else:
        print(0)
        recursive(n)


num = int(input('Enter up to which number of the fibonacci sequence you want to print: '))
fibonacci(num)
