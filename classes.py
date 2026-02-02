classes = {
    "guerreiro": {"vida": 15, "dano": 3, "velocidade": 3, "tipo_habilidade": "golpe contundente","usoHabilidade": 3},
    "assassino": {"vida": 8, "dano": 5, "velocidade": 1, "tipo_habilidade": "golpe sujo","usoHabilidade": 3},
    "arqueiro": {"vida": 10, "dano": 4, "velocidade": 2, "tipo_habilidade": "flecha de gelo","usoHabilidade": 3}
}


def usarHabilidade(escolha):
    print(f"Usando habilidade: {escolha}!")