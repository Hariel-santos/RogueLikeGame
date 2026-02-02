import random
from classes import classes
from jogador import heroi
from inimigos import inimigos
from items import items
from classes import usarHabilidade



def atacar(atacante, defensor):
    defensor["vida"] -= atacante["dano"]
    print(f"O {defensor['nome']} agora tem {defensor['vida']} de vida.")



def equiparItem(jogador, item):
    if item["nome"].lower() == "manopla de força":
        jogador["dano"] += 2
        print(f"Dano aumentado! Dano atual: {jogador['dano']}")
    elif item["nome"].lower() == "armadura de couro":
        jogador["vida"] += 3
        print(f"Vida aumentada! Vida atual: {jogador['vida']}")
    elif item["nome"].lower() == "poção de vida":
        jogador["vida"] += 5
        print(f"Vida aumentada! Vida atual: {jogador['vida']}")


def round(jogador1, jogador2):
    i=0
    atq1 = 0
    atq2 = 0
    while i < 4:
        if jogador1["velocidade"] == atq1:
            escJog = input("É sua vez de atacar! Deseja atacar, defender ou usar habilidade (1, 2 ou 3): ")
            if escJog == "1":
                atacar(jogador1, jogador2)
            elif escJog == "2":
                print("Você bloqueou o ataque!")
                atq2 -= 1
            elif escJog == "3":
                if jogador1["usoHabilidade"] > 0:
                    jogador1["usoHabilidade"] -= 1
                    print("Usando habilidade especial!")
                    usarHabilidade(jogador1["tipo_habilidade"])
                    atq2-=2
                else:
                    print("Você não tem usos de habilidade restantes! e demorou muito tempo pensando...")
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
        heroi.update(classes["guerreiro"])
    elif escolha == "2":
        heroi.update(classes["assassino"])
    elif escolha == "3":
        heroi.update(classes["arqueiro"])
    else:
        print("Classe inválida. Tente novamente.")
    print("Bem-vindo ao jogo de luta heroi!")
    while heroi["vida"] > 0:
        print(f"Um inimigo apareceu! {inimigos[0]['nome']}")
        batalha(heroi, inimigos[0])
        if heroi["vida"] <= 0:
            print("Game Over!")
            break
        continuar = input("Deseja continuar lutando? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por jogar!")
            break
        print(f"Um inimigo apareceu! {inimigos[1]['nome']}")
        batalha(heroi, inimigos[1])
        if heroi["vida"] <= 0:
            print("Game Over!")
            break
        item_encontrado = random.choice(items)
        print(f"Você encontrou um item: {item_encontrado['nome']} - {item_encontrado['efeito']}")
        equiparItem(heroi, item_encontrado)
        print(f"Um inimigo apareceu! {inimigos[2]['nome']}")
        batalha(heroi, inimigos[2])
    print("Fim do jogo.")
