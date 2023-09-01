import random
numero_aleatorio = random.randint(1, 100)
dicamaior = random.randint(1, 10)
dicamenor = random.randint(1, 10)
tentativa = 5
dica = "O seu numero está entre", numero_aleatorio - dicamenor, "e", numero_aleatorio + dicamaior, ", boa sorte!"

print("***********************************************************************")
print(dica)
print("***********************************************************************")
while tentativa > 0:
    chute = input("Digite o numero:")
    chute = int(chute)
    if chute == numero_aleatorio:
        print("Voce acertou !")
        break
    else:
        if(chute > numero_aleatorio):
            print("Seu chute foi MAIOR que o numero")
        elif(chute < numero_aleatorio):
            print("Seu chute foi MENOR que o numero")
    tentativa -= 1
    print("Voce possui", tentativa, "tentativas")
if(tentativa == 0):
    print("Voce não acertou, recomeçe")