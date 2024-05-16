arq = open('texto.txt','r+')

texto = arq.read()
arq.seek(0,0)
tl = list(texto)

for i in range(len(tl)):
    if tl[i] == 'a':
        tl[i] = 'A'

#tl[0]='0'
tl = "".join(tl)
print(tl)

#arq.write(tl)

arq.close()
