#DESAFIO DEV 1 - FAZER UM CÓDIGO QUE RETORNE PARA O USUÁRIO SE UM ANO É BISSEXTO OU NÃO

def entrada_numerica(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("O valor deve ser numérico e inteiro")

def verificacao_ano(ano):
    #VERIFICANDO SE O ANO É CENTENÁRIO
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} NÃO é bissexto")

ano_usuario = 0 #ANO QUE O USUÁRIO VAI ATRIBUIR

while ano_usuario <= 0:
    #TRATATIVA PARA CASO O USUÁRIO NÃO SELECIONE UM NÚMERO INTEIRO E MAIOR QUE ZERO
    ano_usuario = entrada_numerica("Qual o ano deseja verificar se é bissexto: ")
    if ano_usuario <= 0:
        print("Entrada invalida, por favor digite um número inteiro maior do que zero.") 
    else:
        verificacao_ano(ano_usuario)  