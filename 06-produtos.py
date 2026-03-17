import os

os.system("cls")

print("Seja bem vindo a Zero a Zero!")

produto = (input("Digite qual é o produto: "))
quantidade = float(input("Digite quantidade de produto: "))
preco = float(input("Digite preço do produto: "))

total = quantidade * preco 

if(quantidade <= 5):
    desconto = total * 0.02 

elif(quantidade <= 5 and quantidade <= 10):
    desconto = total * 0.03

else:
      desconto = total * 0.05

total_a_pagar = total - desconto

print("-" * 25)
print("Preço total: ", total)
print("Desconto: ", desconto)
print("Total com desconto: ", total_a_pagar)

input("Pressine qualquer tecla para sair.")