import os

os.system("cls")

print("Seja bem vindo para descobrir se seu número é par ou ímpar!")

numero01 = int(input("Digite um número inteiro: "))
 
if numero01 % 2 == 0:
    print("É par.")

else:
    print("É ímpar.")

input("Pressione qualquer tecla para sair.")