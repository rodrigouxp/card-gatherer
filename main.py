from unicodedata import numeric
import pandas as pd

total = int(input('Total de cards da coleção: '))

tabela = pd.read_csv('tabela.csv')
tabela['Card #'] = pd.to_numeric(tabela['Card #'], errors='coerce')

lista_adquiridos = []
lista_faltantes = []

for item in tabela['Card #']:
    if item == 'nan':
        continue
    else:
        if item not in lista_adquiridos and item != 'nan':
            lista_adquiridos.append(item)
        
lista_adquiridos.sort()

for numero in range(total):
    if numero+1 not in lista_adquiridos:
        lista_faltantes.append(numero+1)
        
print(lista_adquiridos)
print()
print(lista_faltantes)
        

