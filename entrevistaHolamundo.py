import executionTime

@executionTime.decorator
def aplana1lvl(array):
    new = []
    for i in array:
        new.extend(i)
    return new


print(aplana1lvl([[1, 2], [[3, 4]], [1, []]]))


def repeated(text, word):
    if not word in text:
        return 0
    l = text.lower().split()
    l.sort()
    inicio = l.index(word)
    fin = len(l) - l[::-1].index(word)
    amount = fin - inicio + 1
    return amount

# """repararar error cuando se repite una vez"""
# text = ("Lorem dolor sit amet, consectetur adipiscing elit. Pellentesque vel mi ut\
# velit tempor aliquam eget eget enim. Proin cursus eleifend pretium. Aliquam cursus \
# pellentesque interdum. Vivamus placerat id leo a pellentesque. Vivamus a congue urna,\
# sed porta eros. Etiam finibus magna et est aliquam, sed semper libero facilisis. \
# Donec lectus lorem, rhoncus vitae quam eget, vulputate gravida elit. Praesent ultricies\
# eros id velit condimentum, eu ultrices nisl consequat.")
# words = ['eget', 'pellentesque', 'lorem', 'velit', 'gravida', 'et', 'limon']
# for word in words:
#     print(word,':',repeated(text, word))
