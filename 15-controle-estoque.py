import os

os.system("cls")

print("Seja bem vindo ao estoque da Zero a Zero!")

produto = (input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade do produto no seu estoque: "))

produto = quantidade

if quantidade <= 5:
    print("Estoque abaixo! ")
else:
     quantidade >=5
     print("Estoque OK. ")

input("Pressione qualquer tecla para sair.")