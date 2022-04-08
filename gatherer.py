import pandas as pd
import sys
from math import isnan
import numpy as np

# Define a função que lê a tabela em .csv
def readTable(tableName):
    table = pd.read_csv(tableName)
    table = table['Card #']
    # Verifica se o card tem o caractere "a" junto ao número e o separa, atribuindo o novo valor à tabela
    for i, card in enumerate(table):
        if 'a' in card:
            temp = table[i].split('a')
            table[i] = temp[0]
    # Transforma os valores da coluna 'Card #' em numéricos
    table = pd.to_numeric(table, errors='coerce')
    # Remove as linhas com valores nulos
    for i, card in enumerate(table):
        if isnan(card):
            table = table.drop(i)
    # Converte os valores para inteiros
    table = table.astype(np.int64)
    return table

# Define a função que prepara a lista de cards adquiridos
def listaAdquiridos(table):
    lista_adquiridos = []
    for item in table:
        if item not in lista_adquiridos:
            lista_adquiridos.append(item)
    lista_adquiridos.sort()
    return lista_adquiridos

# Define a função que prepara a lista de cards faltantes
def listaFaltantes(list, total):
    lista_faltantes = []
    for numero in range(total):
        if numero+1 not in list:
            lista_faltantes.append(numero+1)
    return lista_faltantes


## Programa principal
if len(sys.argv) != 3:
    print(f'USAGE: python <table> <total cards>')
    exit()

tabela = readTable(sys.argv[1])
total = int(sys.argv[2])

adquiridos = listaAdquiridos(tabela)
faltantes = listaFaltantes(adquiridos, total)

print()
print(f'CARDS ADQUIRIDOS: {adquiridos}\nTOTAL: {len(adquiridos)}')
print()
print(f'CARDS FALTANTES: {faltantes}\nTOTAL: {len(faltantes)}')
