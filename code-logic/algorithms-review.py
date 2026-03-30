#revisão do curso de lógica, agora com python

#informe um número, outro número, faça a soma
# apresente par ao usuário

# n1 = int(input('Informe um número: '))
# n2 = int(input('Informe outro número: '))

# soma = n1 + n2

# print (f'A soma entre {n1} e {n2} é {soma}.')

# #media
# n1 = int(input('Informe um número: '))
# n2 = int(input('Informe outro número: '))

# media = (n1 + n2)/2

# print (f'A média entre {n1} e {n2} é {media}.')

#numero absoluto
# numero = -50
# print (abs(numero))

# #exponencial de 5
# numero = 4
# print(pow(numero, 5))

# import math

# numero = 2
# print(math.sqrt(numero))

# numero = int(input('Informe um angulo: '))

# seno = math.sin(numero)

# print (f'O seno de {numero} é {seno}.')

# a = 2
# b = 3
# c = 5

# print (1==c%2)
# print (not ((a==b) or (c>a)))
# input ('Precione enter para sair!')

#triangulos

# l1 = int(input('Digite o primeiro lado do triângulo: '))
# l2 = int(input('Digite o segundo lado do triângulo: '))
# l3 = int(input('Digite o terceiro lado do triângulo: '))

# equilatero = (l1==l2) and (l2==l3) and (l1==l3)
# escaleno = (l1!=l2) and (l2!=l3) and (l1!=l3)
# print (f'''O triânculo é equilátero? {equilatero}
# O triânculo é escaleno? {escaleno}''')

#idade da creuza

# from datetime import datetime 
# ano_atual = datetime.now().year
# ano_nascimento = int(input('Qual seu ano de nascimento? '))
# idade = (ano_atual - ano_nascimento)

# print (f'Sua idade é {idade}.')

#algoritmo de conversão

# reais = float(input('Quantos reais você pode gastar na viagem? '))
# valor_dolar = 5.50
# conversao = round(reais/valor_dolar, 2)

# print (f'Você vai levar {conversao} para a viagem.')

#conversor temperatura

# temperatura_brasil = float(input('Qual a temperatura no Brasil? '))

# temperatura_eua = round(temperatura_brasil/1.8, 1)

# print(f'A temperatura equivalente a do Brasil nos EUA é {temperatura_eua}.')

# #imposto
# valor_compra = float(input('''Qual o valor total das suas compras? 
# $ '''))
# conversao = valor_compra * 5.5
# valor_imposto = conversao * 20/100

# print(f'O valor em reais é {conversao} e o valor dos impostos sobre suas compras é de R$ {valor_imposto}.')

#estruturas condicionais

# dinheiro = float(input('Quanto de dinheiro você tem? R$ '))

# if dinheiro>20000:
#     print('Partiu Disney!')
# else: 
#     falta = 21000-dinheiro
#     print(f'Ainda faltam R${falta} para você cosneguir ir pra Disney.')

# #maioridade
# from datetime import datetime

# ano_atual = datetime.now().year
# ano_nasc = int(input('Em que ano você nasceu? '))

# idade = ano_atual-ano_nasc
# maioridade = 18 - idade 

# if idade >= 18:
#     print("Você atingiu a maioridade. ")
# else:
#     print(f"Ainda faltam {maioridade} para você atingir a maioridade.")

#IMC

# altura = float(input('Sua altura: '))
# peso = float(input('Seu peso: '))

# IMC = peso / altura**2

# if IMC >= 18.5 and 25:
#     print ('Parabéns, você esta no seu peso ideal!')
# else:
#     print ('Você não esta no seu peso ideal.')

#boletim

# nota = int(input('Qual sua nota? '))

# if nota >= 7:
#     print('Você esta aqprovado!')
# else:
#     if nota < 7 and nota >= 5:
#         print ('Você esta em recuperação.')
#     else:
#         print('Você esta reprovado.')

#IMC2

# altura = float(input('Sua altura: '))
# peso = float(input('Seu peso: '))

# IMC = round(peso / altura**2, 2)

# print (IMC)

# if IMC <= 17:
#     print ('Muito abaixo do peso.')
# elif IMC > 17 and IMC < 18.5:
#     print('Abaixo do peso ideal')
# elif IMC >= 18.5 and IMC < 25:
#     print('Peso normal')
# elif IMC >= 25 and IMC < 30:
#     print('Sobrepeso')
# elif IMC >= 30 and IMC < 35:
#     print('Obesidade')
# elif IMC >= 35 and IMC < 40:
#     print('Obesidade severa')
# else:
#     print('Obesidade mórbida')

#match case

# doar = input ('''CRIANÇA ESPERANÇA
# Para fazer sua doação escolha uma das opções abaixo:
# 1 - Para doar 5 reais
# 2 - Para doar 10 reais
# 3 - Para doar 15 reais
# 4 - Para doar 20 reais
# 5 - Para doar um valor superior a 20 reais.
              
# Escolha: ''')

# match doar:
#     case '1':
#         valor = 5
#     case '2':
#         valor = 10
#     case '3':
#         valor = 15
#     case '4':
#         valor = 20
#     case '5':
#         valor = float(input('Qual o valor da sua doação? R$ '))

# print(f'Sua doação no valor de {valor} foi recebida!\nMuito obrigada!')

#dependentes

# import os

# nome = input('Qual seu nome? ')
# matricula = os.getlogin()
# salario = float(input('Qual seu salário? '))
# dependentes = int(input('Qual o número de dependentes? '))

# match dependentes:
#     case 1:
#         salario = salario + (salario * 5/100)
#     case 2, 3, 4:
#         salario = salario + (salario * 10/100)
#     case 5, 6:
#         salario = salario + (salario * 15/100)
#     case _:
#         salario = salario + (salario * 20/100)

# print(f'Sua matrícula é {matricula} e seu salário é {salario} porque você tem {dependentes} dependentes.')

#aproveitamento

# nota1 = float(input('Sua primeira nota: ')) 
# nota2 = float(input('Sua segunda nota: '))

# media = round((nota1 + nota2) /2)

# match media:
#     case 10 | 9:
#         aproveitamento = 'A'
#     case 8 | 7:
#         aproveitamento = 'B'
#     case 6 | 5:
#         aproveitamento = 'C'
#     case 4 | 3:
#         aproveitamento = 'D'
#     case 2 | 1:
#         aproveitamento = 'E'
#     case _:
#         aproveitamento = 'inexistente'
#         print ('Reinicie o programa e digite um valor válido de 0 a 10')

# if 10.0 or 9.0:
#     aproveitamento = 'A'
# elif 8.0 or 7.0:
#     aproveitamento = 'B'
# elif 6.0 or 5.0:
#     aproveitamento = 'C'
# elif 4.0 or 3.0:
#     aproveitamento = 'D'
# elif 2.0 or 1.0:
#     aproveitamento = 'E'
# else: 
#     print ('Digite um valor entre 1 e 10')


# print(f'MÉDIA: {media}')
# print(f'APROVEITAMENTO: {aproveitamento}')

#placar de gols

# time1 = input('Qual time estava jogando nesse fim de semana?')
# time2 = input('Contra qual? ')

# gols1 = int(input(f'Quantos gols o {time1} marcou? '))
# gols2 = int(input(f'Quantos gols o {time2} marcou? '))

# diferenca_gols = gols1 - gols2


# if (diferenca_gols > 0) and (diferenca_gols < 2):
#     resultado = 'normal'
# elif (diferenca_gols > 2) and (diferenca_gols <= 6):
#     resultado = 'goleada'
# elif (diferenca_gols == 0):
#     resultado = 'empate'
# else:
#     resultado = 'Uau!'

# print (f''' {time1}: {gols1}
# {time2}: {gols2}

# RESULTADO: {resultado}''')

#estruturas de repetição

# #while
# contador = 0
# while contador < 10:
#     contador +=1
#     ##contador =contador + 1
#     print(contador)

# usuario = int(input('Até qual número você quer contar? '))

# contador = 0
# while contador < usuario:
#     contador +=1
#     print (contador)

#maior e soma
# n = 0
# contador = 0
# soma = 0
# maior = 0

# while n < 3:
#     n = int(input(f'Digite o {contador} valor: '))
#     soma = soma + n
#     if n > maior:
#         maior = n
#     contador +=1     

# print(f'A soma de todos os valores foi {soma} e o maior valor digitado foi {maior}.')

#contagem regressiva e contagem progressiva


# m = int(input('Contagem a partir de qual número? '))
# n = int(input('Contagem até qual número? '))

# contador = m

# if contador < n:
#     while contador <= n:
#         contador +=1
#         print (f'{contador}...')
# else:
#     while contador >= n:
#         contador -=1
#         print (f'{contador}...')
# print('Fim!')

#melhor aluno da turma

# alunos = int(input('Quantos alunos tem na turma? '))

# contador = 1 
# aluno = 0
# maior = 0 

# while contador <= alunos:
#     aluno = input ('Qual o nome do aluno: ')
#     nota = float(input(f'Qual a nota do {aluno}? '))
#     if nota > maior:
#         maior = nota
#     contador +=1 

# print (f'O melhor aluno da turma é {aluno} com a nota {maior}.')

#while com input de usuário

# soma = 0 
# continuar = 's'

# while continuar == 's':
#     n = int(input('Qual número você quer somar? '))
#     soma = soma + n

#     continuar = input('Você quer continuar (s/n)? ').lower()

# print(f'A soma dos números que você inseriu é {soma}. ')

#contador negativos

# continuar = 'S'
# n = 0
# total_negativos = 0

# while continuar == 'S':
#     n = int(input('Qual número você quer inserir? '))
#     if n < 0:
#         total_negativos = total_negativos + n
    
#     continuar = input('Você quer continuar(S/N)? ').upper()

# print (f'A soma dos números negativos é {total_negativos}.')

#numeros primos

# cont = 1
# total_divisiveis = 0

# numero = int(input('De qual número você quer saber os divisores? '))

# while cont <= numero:
#     if (numero % cont == 0):
#         print (f'O número {numero} é divisível por {cont}.')
#         total_divisiveis = total_divisiveis + 1
#     cont +=1
    
# print(f'O total de números divisíveis por {numero} é {total_divisiveis}.')

# if total_divisiveis > 2:
#     print('Esse número não é primo.')
# else:
#     print ('Esse número é primo.')

# match case e while

# escolha = input('''[1] Se quer contar de 1 a 10
# [2] Se quer contar de 10 a 1
# [3] Sair ''')

# match escolha:
#     case '1':
#         cont = 0
#         while (cont <10):
#             cont +=1
#             print(f'{cont}...')
#     case '2':
#         cont = 11
#         while (cont > 1):
#             cont -=1
#             print(f'{cont}...')
#     case 3:
#         print ('Saindo... ')

#sexo, idade, cor do cabelo

# continuar = 'S'
# total_masculino = 0
# total_feminino = 0

# while continuar == 'S':
#     print ('-------------------------------------')
#     gender = input('Qual o genero (M/F)?' ).upper()
#     print ('-------------------------------------')
#     idade = int(input('Qual a idade? '))
#     print ('-------------------------------------')
#     cabelo = input('''Cor do cabelo:
#     [1] Loiro
#     [2] Castanho
#     [3] Preto
#     [4] Ruivo ''')
#     print ('-------------------------------------')

#     if gender == 'M'and idade < 18 and cabelo == '2':
#         total_masculino = total_masculino + 1

#     elif gender == 'F' and (idade >= 20 and idade <= 30) and cabelo == '1':
#         total_feminino = total_feminino + 1

#     continuar = input('Quer continuar (S/N)? ').upper()
   

# print (f'Total de homens com cabelo castanho e menos de 18 anos {total_masculino}, total de mulheres com cabelo loiro, entre 20 e 30 anos é {total_feminino}.')

#for

# for n in range(1, 10):
#     print(n)

#saber quais numeros são pares

# valor = int(input('Digite um valor: '))

# if valor % 2 == 0:
#     print ('Esse número é par')
# else:
#     print ('Esse número é ímpar')

#quantos valores estão entre um intervalo numérico, nesse caso entre 0 e 10 E a soma entre os valores ímpares digitados

# total_intervalo = 0
# soma_impar = 0

# for n in range (0, 6):
#     valor = int(input('Digite um valor: '))

#     if valor >= 0 and valor <= 10:
#         total_intervalo = total_intervalo + 1
    
#     if valor % 2 != 0:
#         soma_impar = soma_impar + valor

# print (f'Existem {total_intervalo} valores entre 0 e 10. E a soma dos valores ímpares é {soma_impar}.')

#um for dentro de outro for

# for n in range (0, 3):
#     for m in range (0, 3):
#         print(n, m)

#quantos são nulos, quantos são pares e a soma dos pares, media, divisíveis por 5 

nulos = 0
tot_pares = 0
divisivel = 0
soma_valor = 0
soma_pares = 0

for n in range (1, 6):
    valor = int(input(f'Digite o {n}° valor: '))

    if valor == 0:
        nulos = nulos + 1
    elif valor % 2 == 0:
        tot_pares = tot_pares + 1
        soma_pares = soma_pares + valor
    elif valor % 5 == 0:
         divisivel = divisivel + 1
   
    soma_valor = soma_valor + valor
    media = soma_valor / 5

print(f'A soma entre os valores é {soma_valor}')
print (f'A média dos valores inseridos é: {media}')
print (f'O total de números pares é: {tot_pares}')
print (f'O valor da soma dos pares é: {soma_pares}')
print(f'A soma dos valores divisíveis por 5 é: {divisivel}')