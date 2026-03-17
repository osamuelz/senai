import os

os.system("cls")

print("Seja bem vindo professor voçê saberá quanto receberá!")

nivel = int(input("Qual o nível do professor (1, 2 ou 3)? "))
aula = int(input("Quantas aulas ele deu na semana? "))

if(nivel == 1):
    valor_da_hora = 12

elif(nivel == 2):
    valor_da_hora = 17

elif(nivel == 3):
    valor_da_hora = 25
else:
    valor_da_hora = 0

salario_final = valor_da_hora * aula

if(valor_da_hora > 0):
    print("O salário é R$", salario_final)
else:
    print("Erro: Esse nível não existe!")

input("Pressione qualquer tecla para sair.")