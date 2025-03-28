nome_usuario = input("Crie um nome de usuário: ")
senha = input("Crie uma senha: ")

while True:
    if nome_usuario == senha:
        print("ATENÇÃO: Seu nome de usuário e senha não podem ser iguais")
        nome_usuario = input("Crie um nome de usuário: ")
        senha = input("Crie uma senha: ")
    elif nome_usuario != senha:
        print("Login realizado com sucesso!")
    break
