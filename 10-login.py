import os

os.system("cls")

print("Seja bem vindo ao seu computador!")

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "123":
    print("Acesso liberado!")

else:
      print("Acesso negado!")

input("Pressione qualquer tecla para sair.")