import random
print('Seja Bem-vindo ao jogo de adivinhação!')
numEscolhido = random.randint(1, 10)

def verificarChute():
    tentativas=1
    while True: 
        msg='Chute um valor de 1 a 10!'
        chute = int(input(msg))
        if(chute==numEscolhido):
            print('Parabéns!!')
            plTentativa= 'tentativas' if tentativas > 1 else 'tentativa'
            print('Você acertou com {} {}'.format(tentativas, plTentativa))
            
        else:
            if(chute < numEscolhido):
                print(msg, '\nO número é maior!')
            else:
                print(msg,'\nO número é menor!')
        tentativas+=1

verificarChute()