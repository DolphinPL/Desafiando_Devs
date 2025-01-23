#DESAFIO DEV 4 - RETORNANDO O ALFABETO 
import string as s

def entrada_numerica(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("O valor deve ser numérico e inteiro")

alfabeto = list(s.ascii_uppercase)

#Determinar tamanho da array
tamanho = entrada_numerica("Digite um número inteiro de 1 a 26: ")

while 0 >= tamanho or tamanho >26:
    tamanho = entrada_numerica("Obrigatoriamente o número deve estar entre 1 a 26. Digite novamente: ")

resposta =  alfabeto[:tamanho]

print(resposta)