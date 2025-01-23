#DESAFIO DEV 3 - SOMAR 2 MATRIZES

import numpy as np   

def entrada_numerica(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("O valor deve ser numérico, inteiro e maior do que zero")

def contrucao_matriz(dimensao, matriz):
    for i in range(dimensao):
        linha = []
        for coluna in range(dimensao):
            linha.append(entrada_numerica(f"Qual o elemento da linha {i+1} e coluna {coluna+1}:"))
        matriz.append(linha)  
    return matriz  
           
matriz_1 = []
matriz_2 = []

#Receber tamanho das matrizes 
dimensao = entrada_numerica("Qual o numero de linhas/colunas da sua matriz quadrada: ")
while dimensao <= 0:
    print("O valor deve ser maior do que zero. Por favor insira o valor novamente:")
    dimensao = entrada_numerica("Qual o numero de linhas/colunas da sua matriz quadrada: ")

#Contruir a matriz 1
matriz_1 = contrucao_matriz(dimensao, matriz_1)

#Contruir a matriz 2
matriz_2 = contrucao_matriz(dimensao, matriz_2)

#Somar as matrizes
matriz_1 = np.array(matriz_1)
matriz_2 = np.array(matriz_2)
soma_matrizes = matriz_1 + matriz_2

#Imprimir matrizes
print(soma_matrizes)