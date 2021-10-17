def jogar():
    print("************************************")
    print("**** Bem vindo ao jogo de Forca ****")
    print("************************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    index = 0

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip()

        for letra in palavra_secreta:
            if(chute.lower() == letra.lower()):
                print("Letra {} encontrada na posição {}.".format(chute, index))
            index += 1

    print("Fim de jogo!")

#Necessário para execução via Command. Verifica se a execução foi startada a partir dessa classe.
if (__name__ == "__main__"):
    jogar()