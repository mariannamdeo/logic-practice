#qual seu nome?
#qual sua idade?
#se idade>18: maior de idade
#senão: menor de idade

#01
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

if idade >= 18:
    print (f'Olá, {nome}! Sua idade é {idade} e você já esta na maioridade.')
else:
    print (f'Olá, {nome}! {idade} é menor que 18, portanto você ainda não chegou a maioridade.')

#02

#Qual sua nota na matéria?
#Se maior que 7, aprovado
#Se entre 7 e 5, recuperação
#Senão: reprovado

nota = float(input('Qula sua nota na matéria? '))

if nota >= 7:
    print('Aprovado')
elif nota < 7 and nota > 5:
    print ('Recuperação')
else:
    print('Reprovado')
