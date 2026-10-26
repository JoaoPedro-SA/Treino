# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

usuario = ''
senha = ''

def cadastro(): 
     global usuario, senha
     usuario = input("Digita o nome de usuario: ")
     senha = input("Digita a senha: ")

def login(): 
     global usuario, senha
     usuario_login = input("Digite o nome de usuario: ")
     senha_login = input("Digite a senha: ")

     if usuario_login == usuario and senha_login == senha:
          print("Login bem-sucedido!")
     else:
          print("Nome de usuário ou senha incorretos.")

cadastro()
login()
