a='Adição'
s='Subtração'
m='Multiplicação'
d='Divisão'
ex='Sair'
while True:
    opcao=int(input('Escolha uma das opções abaixo:\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n'.format(a,s,m,d,ex)))
    match opcao:
        case 1:
            n1=int(input('Digite o primeiro valor: '))
            n2=int(input('Digite o segundo valor: '))
            print('O resultado da sua operação é: {}.'.format(a, n1+n2))
        case 2:
            n1=int(input('Digite o primeiro valor: '))
            n2=int(input('Digite o segundo valor: '))
            print('O resultado da sua operação é: {}.'.format(s, n1-n2))
        case 3:
            n1=int(input('Digite o primeiro valor: '))
            n2=int(input('Digite o segundo valor: '))
            print('O resultado da sua operação é: {}.'.format(m, n1*n2))
        case 4:
            n1=int(input('Digite o primeiro valor: '))
            n2=int(input('Digite o segundo valor: '))
            if n2 != 0:
                print('O resultado da sua operação é: {}.'.format(d, n1/n2))
            else:
                print('Não é possivel dividir um numero por zero!')
        case 5: 
            print('Saindo...')
            break
        case _:
            print('Opção invalida! Escolha um numero de 1 a 4!')
    print( '-'*30 )