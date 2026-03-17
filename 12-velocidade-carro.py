import os

os.system("cls")

print("Seja bem vindo ao programa que vigia sua velocidade!")

velocidade = float(input("Qual é a velocidade do seu carro em km/h? "))

if velocidade > 80:
    print("Multado!")
else:
    print("Dentro do limite.")

input("Pressione qualquer tecla para sair.")