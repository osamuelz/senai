import os

os.system("cls")

print("Seja bem vindo para saber o intervalo de numeros do 10 ao 15!")

numero = int(input("Digite um número inteiro: "))

if(numero >= 10 and numero <=50):
    print("Você está dentro do intervalo.")
else:
    print("Fora do intervalo.")