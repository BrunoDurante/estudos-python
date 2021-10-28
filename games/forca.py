import random

def jogar():
    print("************************************")
    print("**** Bem vindo ao jogo de Forca ****")
    print("************************************")

    lista = []
    with open("palavra.txt") as arquivo:
        for linha in arquivo:
            lista.append(linha.strip())
    arquivo.close()
    print(lista)
    print(len(lista))

    numeroRandom = random.randrange(0, len(lista))
    print(numeroRandom)
    palavra_secreta = lista[numeroRandom].lower()
    palavra_console = ["_" for letra in palavra_secreta]

#   inteiros = [1, 3, 4, 5, 7, 8, 9]
#   pares = [x for x in inteiros if x % 2 == 0]

    enforcou = False
    acertou = False
    tentativas = 6
    print(palavra_console)

    while (not enforcou and not acertou):
        index = 0
        chute = input("Digite uma letra: ")
        chute = chute.strip().lower()

        if (chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    palavra_console[index] = letra
                index += 1
            print(palavra_console)
        else:
            tentativas -= 1

        acertou = "_" not in palavra_console
        print("Restam {} tentativas.".format(tentativas))
        enforcou = tentativas == 0

    if (acertou):
        print("Parabéns! Você venceu. A palavra é: {}".format(palavra_secreta))
    else:
        print("Fim da linha. Você perdeu.")

    print("Fim de jogo!")


# Necessário para execução via Command. Verifica se a execução foi startada a partir dessa classe.
if (__name__ == "__main__"):
    jogar()
