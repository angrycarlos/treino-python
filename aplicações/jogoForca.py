pl=input('Digite a palavra que a pessoa vai ter que descobrir: ')
separaPalavra = list(pl)
forca = ['_'] * len(separaPalavra)
letrasTentadas = []
tentativas=6
print(forca)

while True:
    chute = input('Digite uma letra: ').lower()

    for i in range(len(separaPalavra)):
        if separaPalavra[i] == chute:
            forca[i] = chute

    print(' '.join(forca))

    if chute not in letrasTentadas:
        letrasTentadas.append(chute)
        print(letrasTentadas)
    else:
        print('Você já tentou essa letra!')

    if chute not in separaPalavra:
        tentativas-=1
        print('Você errou! Tentativas: {}'.format(tentativas))
    if tentativas == 0:
        print('Você perdeu o jogo! Suas tentativas acabaram!')
        break
    if '_' not in forca:
        print('Você venceu! A palavra era: {}'.format(separaPalavra))
        break