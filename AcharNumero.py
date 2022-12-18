
import random

print("Jogo de achar numeros!")

num = input('Digite ate aonde deve ir a aleatoriade de numero! -- ')




if num.isdigit():
    
    num = int(num)

    if num < 0 :
        print('Digite um numero positivo !')
        quit()

else:
    print('Digite um numero da proxima vez !')
    quit()



numAleatorio = random.randint( 0 , num)
tentativas = 0

while True:
        tentativas += 1
        escolhaUsuario = int(input('Digite seu palpite -- '))

        if escolhaUsuario == numAleatorio :
            print('****** PARABENS VOCE ACERTOU ******')
            break
        elif escolhaUsuario > numAleatorio :
            print('Voce esta chegando, é um numero MENOR !')
        elif escolhaUsuario < numAleatorio :
            print('Voce esta chegando é um numero MAIOR ! ')

        

print('Voê levou apenas : ' + str(tentativas) + ' tentativa para encontrar o numero !!')