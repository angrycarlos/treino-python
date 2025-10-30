a='Adição'
s='Subtração'
m='Multiplicação'
d='Divisão'
ex='Sair'
msg1 ='Digite o primeiro valor: '
msg2 = 'Digite o segundo valor: '
msg3 = 'O resultado da sua operação de {} é: {}.'
while True:
    opcao=int(input('Escolha uma das opções abaixo:\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n'.format(a,s,m,d,ex)))
    match opcao:
        case 1:
            n1=int(input(msg1))
            n2=int(input(msg2))
            print(msg3.format(a.lower(), n1+n2))
        case 2:
            n1=int(input(msg1))
            n2=int(input(msg2))
            print(msg3.format(s.lower(), n1-n2))
        case 3:
            n1=int(input(msg1))
            n2=int(input(msg2))
            print(msg3.format(m.lower(), n1*n2))
        case 4:
            n1=int(input(msg1))
            n2=int(input(msg2))
            if n2 != 0:
                print(msg3.format(d.lower(), n1/n2))
            else:
                print('Não é possivel dividir um numero por zero!')
        case 5: 
            print('Saindo...')
            break
        case _:
            print('Opção invalida! Escolha um numero de 1 a 4!')
    print( '-'*30 )