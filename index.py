from random import randint
import time
historico = 0
placa = 0

print("===========================")
print("Vamos jogar par ou impar?")
print("===========================")

player_escolha = input("Digite [Par] ou [Impar]: ").upper()

player_numero = int(input("Digite o número de 0 a 10 que deseja jogar: "))

bot_numero = randint(0, 10)

final = ""

resultado = player_numero + bot_numero

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


def historico_final(historico, final):
    msg, final = resultado_final(player_escolha, resultado)
    if final == "venceu":
        voce += 1
    elif final == "perdeu":
        computador += 1
    
    mensagem = (f"você venceu {voce} vezes e {computador} vezes.")

    return mensagem, voce, computador

msg, final = resultado_final(player_escolha, resultado)

msg_historico = resultado_final(player_escolha, resultado)

while player_escolha != "PARAR":

    historico += 1
    print(msg)

    player_escolha = input("Deseja continuar? Digite [SIM] para continuar ou [NAO] para parar e ver seu histórico: ").upper()

    if player_escolha == "SIM":
        player_escolha = input("Digite [Par] ou [Impar]: ").upper()

        player_numero = int(input("Digite o número de 0 a 10 que deseja jogar: "))

    else:
        break

print(msg_historico)
print(historico)
 





