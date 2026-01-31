import random
from classes import classes


jogador = {
    "nome": "Heroi",
    "vida": 10,
    "dano": 2,
    "velocidade": 2,
    "mochila": [3]
    }

def atacar(atacante, defensor):
    defensor["vida"] -= atacante["dano"]
    print(f"O {defensor['nome']} agora tem {defensor['vida']} de vida.")

def usarItem(jogador):
    print("Itens na mochila:", jogador["mochila"])
    print("Você usou um item de cura!")
    jogador["vida"] += 5
    jogador["mochila"].pop(-1)



def round(jogador1, jogador2):
    i=0
    atq1 = 0
    atq2 = 0
    while i < 4:
        if jogador1["velocidade"] == atq1:
            escJog = input("É sua vez de atacar! Deseja atacar ou usar item (1 ou 2): ")
            if escJog == "1":
                atacar(jogador1, jogador2)
            else:
                print("Você bloqueou o ataque!")
                usarItem(jogador1)
            atq1 = 0
        if jogador2["velocidade"] == atq2:
            print("inimigo ataca!")
            atacar(jogador2, jogador1)
            atq2 = 0
        atq1+=1
        atq2+=1
        i+=1
        
def batalha(jogador1, jogador2):
    while jogador1["vida"] > 0 and jogador2["vida"] > 0:
        if jogador1["vida"] <= 0:
                print("Voce morreu!")
                return
        elif jogador2["vida"] <= 0:
                print("Você venceu o inimigo!")
                return
        round(jogador1, jogador2)
        print("----- Próximo Round -----")

while True:
    escolha = input("Escolha sua classe (guerreiro =1 , assasino=2, arqueiro=3): ")
    if escolha == "1":
        jogador.update(classes["guerreiro"])
    elif escolha == "2":
        jogador.update(classes["assassino"])
    elif escolha == "3":
        jogador.update(classes["arqueiro"])
    else:
        print("Classe inválida. Tente novamente.")
    print("Bem-vindo ao jogo de luta!", jogador)
    while jogador["vida"] > 0:
        inimigo = {
            "nome": "Inimigo",
            "vida": random.randint(5, 15),
            "dano": random.randint(1, 4),
            "velocidade": random.randint(1, 3)
        }
        print(f"Um inimigo apareceu! {inimigo}")
        batalha(jogador, inimigo)
        if jogador["vida"] <= 0:
            print("Game Over!")
            break
        continuar = input("Deseja continuar lutando? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por jogar!")
            break