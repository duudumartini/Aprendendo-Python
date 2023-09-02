print("********************************************************")
print("************* Bem vindo ao jogo de Forca ***************")
print("********************************************************")

palavra_secreta = "banana"
palavra_secreta = palavra_secreta.upper()
letras_acertadas = ["_", "_", "_", "_", "_", "_", ]
segredo = "_"
chances = 5
enforcou = False
acertou = False
posicao = 0

while(enforcou == False and acertou == False):
    print(letras_acertadas)
    print("Sua palavra possui {} letras".format(len(letras_acertadas)))
    chute = input("Qual a letra? ")
    chute = chute.strip()
    chute = chute.upper()
    posicao = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[posicao] = letra
        posicao += 1