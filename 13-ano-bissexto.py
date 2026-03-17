import os

os.system("cls")

print("Seja bem vindo ao calculo dos anos bissexto.")

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Ano bissexto!")
else:
    print("Não é bissexto.")

input("Pressione qualquer tecla para sair.")