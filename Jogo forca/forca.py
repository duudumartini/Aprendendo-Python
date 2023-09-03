import random

def mensagemAbertura():
    print("********************************************************")
    print("************* Bem vindo ao jogo de Forca ***************")
    print("********************************************************")

def CarregaPalavrasSecretas():
    arquivo = open("Jogo forca\palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    return palavra_secreta

mensagemAbertura()

palavra_secreta = CarregaPalavrasSecretas()

lista = ["_" for letra in palavra_secreta]

chances = 10
enforcou = False
acertou = False
posicao = 0

while(enforcou == False and acertou == False):
    print("-----------------------------------------------")
    print(lista)
    print("Sua palavra possui {} letras".format(len(lista)))
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute == letra):
                lista[posicao] = letra
            posicao += 1
    else:
        chances-=1
        print("Voce ERROU ! Não existe a letra {} na palavra secreta".format(chute))
        print("Voce possui mais {} chances".format(chances))

    if(chances==0):
        enforcou=True

    acertou = "_" not in lista

    
        
if(enforcou==True):
    print("-------------------------------------------------")
    print("Voce Perdeu !")  
    print("A palavra secreta era ", palavra_secreta)
    print("-------------------------------------------------")

if(acertou==True):
    print("-------------------------------------------------")
    print(lista)
    print("Voce ganhou !")
    print("A palavra secreta era ", palavra_secreta)
    print("-------------------------------------------------")

