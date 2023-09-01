print("********************************************************")
print("************* Bem vindo ao jogo de Forca ***************")
print("********************************************************")

palavra_secreta = "banana"
enforcou = False
acertou = False
posicao = 1

while(enforcou == False and acertou == False):
    chute = input("Qual a letra? ")
    chute = chute.strip()
    chute = chute.lower()
    posicao = 1
    for letra in palavra_secreta:
        if(chute == letra):
            print("Econtrei a letra {} na posição {}".format(letra, posicao))
        posicao += 1