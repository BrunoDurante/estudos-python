def notes():
    number = 11/3
    print("O number arredondado é {}".format(round(number)))
    print("O number formatado com 2 casas decimais, fica {:.2f}".format(number))
    print("O number formatado com 2 casas decimais, fica {:07f}".format(number))

    print("R$ {:07d}".format(44))
    print("R$ {:07.3f}".format(44.32))
    print("Data é {:02d}/{:02d}".format(21,5))
    print("Meu nome ao contrário é {1} {0}".format("bruno","durante"))

    dia_ini = 24
    dia_fim = 28
    mes = "fevereiro"
    ano = 2017
    print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))

    for numero in range(1,10,2):
        print(numero)


def jogar():
    import random

    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")

    numero_secreto = round(random.randrange(1, 101))
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Digite: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel ==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(total_de_tentativas):
        print("Tentativa {} de {}".format(rodada + 1, total_de_tentativas))
        tentativa_str = input("Digite o seu número: ")
        chute = int(tentativa_str)
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if (acertou):
            print("Você acertou! Fez um total de {} pontos :)".format(pontos))
            break
        else:
            if (maior):
                print("Seu chute foi alto, tente chutar um valor menor.")
            elif (menor):
                print("Seu chute foi baixo, tente chutar um valor maior.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Fim do game!")
    print("Número sorteado:", numero_secreto)

#Necessário para execução via Command
if (__name__ == "__main__"):
    notes()
    jogar()

