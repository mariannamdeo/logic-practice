#for: eu sei a quantidade de vezes em que vou fazer alguma coisa. percorrer uma lista de valores ou letras de uma palavra.
#while: até que alguma condição apareça

# #01
# for numero in range(0, 6):
#     print(numero)

# #02
# compras = ['arroz', 'feijão', 'farinha', 'ovos', 'açucar']

# for item in compras:
#     print(f'Comprar: {item}')

# #03
# palavra = 'comunidade'

# for letra in palavra:
#     print (letra)

#04
# contador = 6

# while contador > 1:
#     contador -= 1
#     print (contador)
# print ('final')

#05

# senha_correta = '1234'
# senha = ''

# while senha != senha_correta:
#     senha = input ('Digite sua senha: ')
#     print ('A senha digitada esta errada. Tente novamente!')
# print ('Senha correta. Acesso autorizado!')

#06

# for numero in range(0,11):
#     print (numero)

#07

# numero = 0

# while numero < 10:
#     numero +=1
#     print(numero)

#08

# for numero in range(1,11):
#     novo_numero = numero * 2
#     print (f'2 x {numero} = {novo_numero}')

#09

# numero = 0

# while numero < 10:
#     numero +=1
#     novo_numero = numero * 3
#     print (f'3 x {numero} = {novo_numero}')

#10

# numero = int(input('De qual número você quer saber o quadruplo? '))

# novo_numero = numero * 4

# print(f'O quadruplo de {numero} é {novo_numero}.')

#11

# tabuada = int(input('Você quer saber a tabuada de qual número? '))

# for numero in range (1,11):
#     novo_numero = numero * tabuada
#     print (f'{tabuada} * {numero} = {novo_numero}')
# print('Fim.')

#12

# multiplicar = int(input('Você quer multiplicar até qual número? '))

# for n in range (1, multiplicar+1):
#     nova_multiplicacao = n * 2
#     print(f'2 x {n} = {nova_multiplicacao}')

#13

usuario = ''

while usuario != 'não':
    usuario = input('Você quer continuar? ')
print ('Fechando o programa!')