import os

os.system("cls")

print("Seja bem vindo ao seu tempo de estudo!")

horas = float(input("Quantas horas você estuda por dia? "))

if horas < 2:
    print("Pouco estudo.")
elif horas <= 3:
    print("Estudo médio.")
else:
    print("Muito estudo!")

input("Pressione qualquer tecla para sair.")