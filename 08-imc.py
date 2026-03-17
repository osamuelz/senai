import os

os.system("cls")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

print(f"Seu IMC é {imc:.1f}")

if imc < 11.4:
    print("Classificação: Muito abaixo do peso.")
elif imc < 16.4:
    print("Classificação: Abaixo do peso.")
elif imc < 20.9:
    print("Classificação: Peso normal.")
elif imc < 30.9:
    print("Classificação: Acima do peso.")
elif imc < 35:
    print("Classificação: Muito acima do peso.")
elif imc < 40:
    print("Classificação: Obesidade Grau I.")
else:
    print("Obesidade Grau II")

input("Pressione qualquer tecla para sair.")