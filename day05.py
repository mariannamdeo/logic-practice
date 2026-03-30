# #união de conceitos
#01
# palavra = 'Python'
# for letra in palavra:
#     if letra == 'y':
#         print('Nessa palavra existe a letra Y!')
#02
# palavra = 'MARIANNA'
# cont = 0
# letra_procurada = input('Qual letra você esta procurando na palavra? ').upper()
#03
# for l in palavra:
#     if l == letra_procurada:
#         print(f'A letra {letra_procurada} existe nessa palavra!')
#         cont = cont+1

# if cont == 0:
#     print('Não existe essa letra nessa palavra. ')

#jogo da adivinhação, 04
# no jogo a pessoa precisa tentar adivinhar o número até acertar

# adivinha = 0
# numero_secreto = 8

# while adivinha != numero_secreto:
#     adivinha = int(input('Tente adivinhar o número secreto! Dica: ele é maior que 0 e vai até 10.'))

#     if adivinha < 5:
#         print ('O número esta longe daí!')
#     elif adivinha >= 5 and adivinha < 8:
#         print ('Esta chegando perto!')
#     elif adivinha > 8:
#         print ('Você esta perto!')
#     else:
#         print ('Parabéns, você liberou o portal!')

#caixa eletrônico, 06
# o usuário pode usar o dinheiro e sacar até encerrar o saldo

saldo = 500
continuar = ''

while saldo >= 0:
    continuar = input ('Quer sacar dinheiro (S/N)? ').upper()
    if continuar == 'S' and saldo!=0:
        saque = float(input ('Quanto você quer sacar? R$ '))
        saldo = round(saldo - saque, 2)
        print (f'Seu saldo atual é de R$ {saldo}.') 
    elif saldo == 0 or continuar == 'N':
        print ('Fim da operação!')
        break


