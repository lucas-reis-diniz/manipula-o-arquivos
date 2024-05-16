import pickle
arq = open('arquivob.bin','wb')

lista = [i for i in range(100)]
#print(lista)

pickle.dump(lista,arq)
arq.close()
