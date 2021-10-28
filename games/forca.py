import random


# notes
# inteiros = [1, 3, 4, 5, 7, 8, 9]
# pares = [x for x in inteiros if x % 2 == 0]

def jogar():
    imprime_mensagem_inicial()
    palavra_secreta = carrega_palavra_secreta()
    print(palavra_secreta)
    palavra_secreta = carrega_palavra_secreta("cores.txt") #apenas testando pâmetros opcionais
    print(palavra_secreta)

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = input_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        acertou = "_" not in letras_acertadas
        enforcou = erros == 7

    if (acertou):
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palavra_secreta)


def imprime_mensagem_inicial():
    print("************************************")
    print("**** Bem vindo ao jogo de Forca ****")
    print("************************************")


def carrega_palavra_secreta(nome_arquivo="frutas.txt"):
    lista = []
    with open(nome_arquivo) as arquivo:
        for linha in arquivo:
            lista.append(linha.strip())
    arquivo.close()
    numeroRandom = random.randrange(0, len(lista))
    return lista[numeroRandom].lower()


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def input_chute():
    return input("Digite uma letra: ").strip().lower()


def marca_chute_correto(chute, palavra, letras_acertadas):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1
    print(letras_acertadas)


def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_derrota(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}.".format(palavra))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Necessário para execução via Command. Verifica se a execução foi iniciada a partir dessa classe.
if (__name__ == "__main__"):
    jogar()
