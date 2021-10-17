def jogar():
    print("************************************")
    print("**** Bem vindo ao jogo de Forca ****")
    print("************************************")

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Selecione a dificuldade: "))

    print("Fim de jogo!")

#Necessário para execução via Command
if (__name__ == "__main__"):
    jogar()