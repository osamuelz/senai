
import os

os.system("cls")

print("Seja bem vindo ao seu boletim virtual!")

nota01 = float(input("Digite a primeira nota:"))
nota02 = float(input("Digite a segunda nota:"))
nota03 = float(input("Digite a terceira nota:"))

media = (nota01 + nota02 + nota03) / 3

print("Sua média é:", media)

if(media>=7):
    print("Você foi aprovado.")
    
elif(media>=4 and media <=6):
    print("Você está de recuperação.")

else:
    print("Você foi reprovado.")
