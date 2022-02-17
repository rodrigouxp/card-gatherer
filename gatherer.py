from unicodedata import numeric
import pandas as pd
import sys

# Define a função que lê a tabela em .csv
def readTable(tableName):
    tabela = pd.read_csv(tableName)
    tabela['Card #'] = pd.to_numeric(tabela['Card #'], errors='coerce')
    return tabela['Card #']


# Define a função que prepara a lista de cards adquiridos
def listaAdquiridos(tabelaCard):

    lista_adquiridos = []

    for item in tabelaCard:
        if item not in lista_adquiridos:
            lista_adquiridos.append(item)
            
    lista_adquiridos.sort()
    return lista_adquiridos

# Define a função que prepara a lista de cards faltantes
def listaFaltantes(lista, total):
    
    lista_faltantes = []
    
    for numero in range(total):
        if numero+1 not in lista:
            lista_faltantes.append(numero+1)

    return lista_faltantes


## Programa principal
if len(sys.argv) != 3:
    print(f'USAGE: python <table> <total cards>')
    exit()

tabelaCard = readTable(sys.argv[1])
total = int(sys.argv[2])

adquiridos = listaAdquiridos(tabelaCard)
faltantes = listaFaltantes(adquiridos, total)

print(f'CARDS ADQUIRIDOS: {adquiridos}')
print()
print(f'CARDS FALTANTES: {faltantes}')
        
