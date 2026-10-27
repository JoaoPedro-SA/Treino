"""
1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
"""

pessoa = ( {"nome": "Alice", "idade": 30, "cidade": "São Paulo"} )

print("Informações da pessoa:")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")