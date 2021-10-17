import adivinhacao
import forca

print("************************************")
print("******* Bem vindo aos jogos ********")
print("************************************")

print("(1) Adivinhação (2) Forca")
jogo = int(input("Selecione o jogo: "))

if(jogo == 1):
    print("Iniciando jogo de Adivinhação...")
    adivinhacao.jogar()
elif(jogo == 2):
    print("Iniciando jogo de Forca...")
    forca.jogar()

