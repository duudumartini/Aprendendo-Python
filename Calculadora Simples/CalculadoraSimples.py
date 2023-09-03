def Somar(Numero1, Numero2):
    resultado = Numero1 + Numero2
    return resultado

def Subtracao(Numero1, Numero2):
    resultado = Numero1 - Numero2
    return resultado

def Divisao(Numero1, Numero2):
    resultado = Numero1 / Numero2
    return resultado

def Multiplicacao(Numero1, Numero2):
    resultado = Numero1 * Numero2
    return resultado

continuar = True

while continuar == True:
    print("Qual operacao deseja realizar ?")
    operacao = int(input("(1) Soma, (2) Subtração, (3)Divisão, (4) Multiplicação"))
    if(operacao == 1):
        Numero1 = int(input("Qual o primeiro numero que deseja somar ?"))
        Numero2 = int(input("Qual o segundo numero que deseja somar ?"))
        print("O resultado da soma é ",Somar(Numero1, Numero2))
    if(operacao == 2):
        Numero1 = int(input("Qual o primeiro numero que deseja subtrair ?"))
        Numero2 = int(input("Qual o segundo numero que deseja subtrair ?"))
        print("O resultado da subtração é ",Subtracao(Numero1, Numero2))
    if(operacao == 3):
        Numero1 = int(input("Qual o primeiro numero que deseja dividir ?"))
        Numero2 = int(input("Qual o segundo numero que deseja dividir ?"))
        print("O resultado da divisão é ",Divisao(Numero1, Numero2))
    if(operacao == 4):
        Numero1 = int(input("Qual o primeiro numero que deseja multiplicar ?"))
        Numero2 = int(input("Qual o segundo numero que deseja multiplicar ?"))
        print("O resultado da multiplicação é ",Multiplicacao(Numero1, Numero2))
    print("Deseja realizar outra operação?")
    continuar = input("(S) sim, (N) não").upper() == "S"



