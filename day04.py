#listas 

#01
lista = [1, 2, 3, 4, 5]

print (lista[0])

lista.append(10)

print (lista)

lista.insert(4, 100)

print (lista)

#02

lista = [1, 2, 3, 4, 5]

lista.pop(3)

print(lista)

lista.remove(2)

print(lista)

#03

lista_numeros = [0, 1, 2, 3, 4, 5, 50, 55, 60, 67]

# #maior numero da lista
print (max(lista_numeros))

# #menor numero da lista
print (min(lista_numeros))

#pedir 5 numeros, guardar em uma lista

user_list = []

for i in range (0,5):
    user_list.append(int(input('Escreva um número: ')))

print (user_list)