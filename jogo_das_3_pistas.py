dicionario = {
    "machado": {
        "dica_1": "é um sobrenome",
        "dica_2": "corta madeira",
        "dica_3": "de assis"
    },
    "são paulo": {
        "dica_1": "nome de santo",
        "dica_2": "nome de cidade",
        "dica_3": "nome de time"
    }
}

for palavra_secreta, dicas in dicionario.items():
    print(f"DICA 1: {dicas['dica_1']}")
    chute_usuario = input('Digite a palavra secreta: ')
    if chute_usuario == palavra_secreta:
        print('parabéns. Acertou')
    # ERRO DICA 1
    else:
        print('Você errou.')
        print(f"DICA 2: {dicas['dica_2']}")
        chute_usuario = input('Digite a palavra secreta: ')
        if chute_usuario == palavra_secreta:
            print('parabéns. Acertou')
        # ERRO DICA 2    
        else:
            print('Você errou.')
            print(f"DICA 3: {dicas['dica_3']}")
            chute_usuario = input('Digite a palavra secreta: ')
            if chute_usuario == palavra_secreta:
                print('parabéns. Acertou')
            # ERRO DICA 3
            else:
                print('Você errou.')


