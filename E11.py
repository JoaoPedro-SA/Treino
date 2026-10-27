"""
7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

"""

lista = [1, 2, 3, 4, 5]

soma = 0

for i in lista:
    soma += i

print ("Media: ", soma / len(lista)) 