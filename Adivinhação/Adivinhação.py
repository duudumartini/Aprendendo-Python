numero_secreto = 43
chances = 5



while chances > 0:
    chute = input("Digite o seu numero:")
    print("Voce digitou", chute)
    chute = int(chute)
    if(numero_secreto == chute):
        print("Voce acertou !")
        break
    else:
        if(chute > numero_secreto):
            print("Voce errou, seu chute foi maior que o numero secreto!")
            chances -=1
            print("voce possui mais", chances, "chances.")
        else:
            print("Voce errou, seu numero foi menor que o numero secreto")
            chances -=1
            print("voce possui mais", chances, "chances.")

if(chances == 0):
    print("Voce perdeu!")
