matriz = eval(input("Ingrese una matriz \n"))
d1 = []
d2 = []
c = -1
m = 1
for i in range(len(matriz)):
    d1.append(matriz[i][i])
for j in range(len(matriz)):
    d2.append(matriz[j][c])
    c -= 1
for k in range(len(d1)):
    m = m*d1[k]*d2[k]
print(m)