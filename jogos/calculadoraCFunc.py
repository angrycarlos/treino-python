
def calculadora(op, n1, n2):
    operações = {
        1: (n1 + n2, 'adição'),
        2: (n1 - n2, 'subtração'),
        3: (n1 * n2, 'multiplicação'),
        4: (n1 / n2 if n2 != 0 else 'Não há divisão por zero', 'divisão')
    }
    return operações.get(op,('Opção invalida', None))

while True: 
    print('Escolha uma das opções abaixo:\n' \
    '1 - Adição\n' \
    '2 - Subtração\n' \
    '3 - Multiplicação\n' \
    '4 - Divisão\n' \
    '5 - Sair' \
    '')

    try:
        opcao=int(input('Digite o número da operação:\n'))
    except ValueError:
        print('Valor inválido, digite o número da operação!')
        continue
    if opcao == 5:
        print('Saindo...')
        break

    if opcao in (1,2,3,4):
        n1=float(input('Digite o primeiro valor: '))
        n2=float(input('Digite o segundo valor: '))
        resultado, nome = calculadora(opcao, n1, n2)
        print('O resultado da sua operação de {} é {}'.format(nome, resultado))
    else:
        print('Opção inválida! Escolha de 1 a 5')

    print('-'*30)