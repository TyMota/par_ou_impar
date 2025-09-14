from random import randint
import time
historico = 0
placa = 0

print("===========================")
print("Vamos jogar par ou impar?")
print("===========================")


final = ""

resultado = 0

voce = 0

computador = 0

player_escolha = ""

def resultado_final(player_escolha, resultado):
    if resultado % 2 == 0:
        if player_escolha == "PAR":
            final = "venceu"
        else:
            final = "perdeu"
    else:
        if player_escolha == "PAR":
            final = "perdeu"
        else:
            final = "venceu"
        

    mensagem = (f"Você escolheu {player_escolha} e deu {resultado}! Você {final}!")

    return mensagem, final

player_escolha = input("Digite [Par] ou [Impar]: ").upper()

while player_escolha not in ["PAR", "IMPAR"]:
    player_escolha = input("Opção errada! Digite [Par] ou [Impar]: ").upper()
    
player_numero = int(input("Digite o número de 0 a 10 que deseja jogar: "))
while player_numero < 0 or player_numero > 10:
    player_numero = int(input("Opção invalida! Digite um número entre 0 e 10: "))

while player_escolha != "NAO":

    bot_numero = randint(0, 10)

    resultado = player_numero + bot_numero

    msg, final = resultado_final(player_escolha, resultado)

    print(msg)

    if final == "venceu":
        voce += 1
    elif final == "perdeu":
        computador += 1

    historico += 1

    player_escolha = input("Deseja contiunar jogando? Digite [Sim] ou [Nao]: ").upper()
    while player_escolha not in ["SIM", "NAO"]:
        player_escolha = input("Opção invalida! Escolha entre [Sim] ou [Nao]: ")

    if player_escolha == "SIM":
        player_escolha = input("Digite [Par] ou [Impar]: ").upper()
        while player_escolha not in ["PAR", "IMPAR"]:
            player_escolha = input("Opção errada! Digite [Par] ou [Impar]: ").upper()

        player_numero = int(input("Digite o número de 0 a 10 que deseja jogar: "))
        while player_numero < 0 or player_numero > 10:
            player_numero = int(input("Opção invalida! Digite um número entre 0 e 10: "))

    else:
        break

print("Fim do programa!")
if historico == 1:
    print(f"Foram jogadas {historico} partida. Você ganhou {voce} veze e o computador {computador} veze.")
else:
    print(f"Foram jogadas {historico} partidas. Você ganhou {voce} vezes e o computador {computador} vezes.")
 





