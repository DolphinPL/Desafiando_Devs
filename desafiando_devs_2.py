#DESAFIO DEV 2 - FUNÇÃO QUE RETORNE UMA EQUAÇÃO DE SEGUNDO GRAU
import math

def entrada_numerica(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("O valor deve ser numérico")
            
def eq_2grau(a,b,c):
    # DESCOBRIR DELTA E SUA RAIZ (B² - 4AC)
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Delta é negativo, logo a equação não possui raízes reais.")
    else:    
        raiz_delta = math.sqrt(delta)
        
        # RESOLVER A EQUAÇÃO (-B +- RAIZ(DELTA))/2A
        x1 = (-b + raiz_delta)/(2*a)
        x2 = (-b - raiz_delta)/(2*a)

        #EXIBIR RESULTADOS
        print(f"\nX1 = {x1}\nX2 = {x2}")

# DEFINIR VARIÁVEIS
a = entrada_numerica("Defina o valor de a (Deve ser diferente de zero): ")
while a ==0: #Na equação de segundo grau o a não pode ser zero
    a = entrada_numerica("O valor deve ser diferente de zero. Digite o novo valor de a: ")
    
b = entrada_numerica("Defina o valor de b: ")
c = entrada_numerica("Defina o valor de c: ")

eq_2grau(a,b,c)