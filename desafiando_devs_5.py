#DESAFIO DEV 5 - MONTAR UM TRIÂNGULO DE *
def entrada_numerica(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("O valor deve ser numérico e inteiro")
            
dimencao = entrada_numerica("Digite o tamanho dos lados do triângulo: ")

while dimencao <= 0:
    dimencao = entrada_numerica("O valor deve ser maior do que zero, Digite o novo valor: ")
    
for i in range(dimencao):
    for linha in range(i+1):
        print("*",end = "") #Para não pular linha
    print() #Para pular linha 