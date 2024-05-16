arq = open(r'arq_ex.csv',encoding='UTF-8')

csv = arq.readlines()

matriz = []
for i in range(len(csv)):
    csv[i] = csv[i].replace('\n','')
    csv[i] = csv[i].replace('\ufeff','')
    #print(csv[i])
    elemn = csv[i].split(',')
    #print(elemn)
    matriz.append(elemn)

print(matriz)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f'{matriz[i][j]:10s}',end='' )
    print()

arq.close()
