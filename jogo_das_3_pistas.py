dicionario = {
    "machado": {
        "dica_1": "é um sobrenome",
        "dica_2": "corta madeira",
        "dica_3": "de assis"
    }
}

for palavra_secreta, dicas in dicionario.items():
    print(f"DICA 1: {dicas['dica_1']}")
    chute_usuario = input('Digite a palavra secreta: ')
    if chute_usuario == palavra_secreta:
        print('parabéns. Acertou')

    else:
        print('Você errou.')
        print(f"DICA 2: {dicas['dica_2']}")
        chute_usuario = input('Digite a palavra secreta: ')
        if chute_usuario == palavra_secreta:
            print('parabéns. Acertou')
        else:
            print('Você errou.')


