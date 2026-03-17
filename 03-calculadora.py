import os

os.system("cls")

print("Seja bem vindo a calculadora!")

operacao = (input("Escolha a sua operação" \
" (+)soma" \
"  (-)subtração" \
"  (/)divisão" \
"  (*)vezes : "))

numero01 = float(input("Digite um número:"))
numero02 = float(input("Digite outro número:"))

if(operacao == "+"): 
    resultado = numero01 + numero02

elif(operacao == "-"):
    resultado = numero01 - numero02

elif(operacao == "*"):
    resultado = numero01 * numero02

elif(operacao == "/"):
    resultado = numero01 / numero02

else:
    print("Não existe essa opção de operação.")

print("O resultado é:", resultado)

input("Pressione qualquer tecla para encerrar.")