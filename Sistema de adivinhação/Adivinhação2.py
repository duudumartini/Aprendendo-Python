numero_secreto = 43
acertou = True

while not acertou:
    chute = input("Digite o seu número: ")
    print("Você digitou", chute)
    chute = int(chute)

    if numero_secreto == chute:
        print("Você acertou!")
        acertou = True  # Define acertou como True para sair do loop
    else:
        print("Você errou!")
if (acertou == True):
    print("Acabou!")