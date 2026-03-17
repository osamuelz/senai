import os

os.system("cls")

print("Seja bem vindo para saber quantos litros gastou percorrendo com seu carro!")

distancia = float(input("Quantos quilômetros você percorreu? "))
gasolina = float(input("Quantos litros de gasolina você usou? "))

resultado = distancia / gasolina

print(f"Seu carro faz {resultado:.1f} km com cada litro!")

input("Pressione qualquer tecla para sair.")