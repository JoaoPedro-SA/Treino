"""3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10."""

num = 0

for i in range(1,11):
    if i % 2 != 0:
            num += i
            print (num) 