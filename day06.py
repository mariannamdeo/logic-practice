#funções steph
# #01
# def soma (a, b):
#      return a + b

# resultado = soma (2, 3)

# print (f'O resultado da soma é {resultado}.')

# #02
# def mensagem (nome):
#      print (f'Olá, {nome}.')

# saudacao = mensagem('Marianna')

#função iniciando com def tem o nome e o recebimento do parâmetro dentro do parenteses
#variavel recebe a chamada da função com o parâmetro sendo passado dentro do parenteses

#03 calcular media

# def media (a, b):
#     return (a + b) /2

# resultado = media (4, 4) #atribuir o retorno da função a variavel e utilizar a variavel 

# print (f'O resultado dessa média é {resultado}.')

#codewars

# def remove_char(s):
#     return s[1:-1]

#Curso em Vídeo

# def soma(a, b):
#     return a + b

# numero1 = int(input('Digite um número: '))
# numero2 = int(input('Digite outro número: '))

# resultado = soma (numero1, numero2)

# print (resultado)

#vetores

#colocar valores nas posições dos vetores

# lista = []

# for n in range (0, 5):
#     lista. append(int (input ('Acrecente um valor na lista: ')))

# print (lista)

#lista par, lista impar

# total_par = 0
# total_impar = 0
# lista_par = []
# lista_impar = []

# for n in range (0, 5):
#     numero = int(input('Digite um número: '))
#     if numero % 2 == 0:
#         total_par = total_par + 1
#         lista_par.append(numero)
#     else:
#         total_impar = total_impar + 1
#         lista_impar.append(numero)

# print (f'A lista dos números pares é {lista_par}, com um total de {total_par} números e a lista ímpar é {lista_impar}, com um total de {total_impar} números.')

#aluno, nota1, nota2, coloca em uma lista a média - aluno, nota1, nota2, coloca em uma lista a média
#o ideal seria usar dicionário, mas essa estrutura não foi ensinada nos cursos da steph que estou usando para python
# alunos = []

# turma = int(input('Quantos alunos tem na turma? '))

# for n in range (0, turma):
#     nome = input('Nome do aluno: ')
#     nota1 = float(input('Primeira nota: '))
#     nota2 = float(input('Segunda nota: '))
    
#     media = nota1+nota2/2

#     alunos.append(media)

# print (f'Notas dos alunos: {alunos}')