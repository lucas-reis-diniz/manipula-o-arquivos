import datetime


data = datetime.datetime.now().strftime('%Y-%m-%d')
nome = f'Nome_do_arquivo_{data}.csv'
print(nome)
