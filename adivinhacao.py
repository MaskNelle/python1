import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int (input("Defina o nível: "))

if nivel == 1:
    total = 20
elif nivel == 2:
    total = 10
else:
    total = 5

for rodada in range(1, total + 1):
    print("Tentativa {} de {}".format(rodada, total))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acerto = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acerto):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
            if rodada == total:
                print("O número secreto era {}, você pontuou {}".format(numero_secreto, pontos))
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
            if rodada == total:
                print("O número secreto era {}, você pontuou {}".format(numero_secreto, pontos))
        pontos_perdidos = abs(chute - numero_secreto) / 3
        pontos = pontos - round(pontos_perdidos)

print("Fim do jogo")
