"""
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
"""

lista = [1, 2, 3, 4, 5]

soma = 0 
for i in lista:
     try:
          soma += i 
          print(soma)
     except  TypeError:   
          print( "ERRO: " )