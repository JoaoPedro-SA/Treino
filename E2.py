# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

idade = int(input("Digita sua idade:"))

if idade < 13: 
    print("Criança")
elif idade < 20:
    print("Adolescente")
else:
    print("Adulto")