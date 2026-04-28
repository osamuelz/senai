
print("seja bem vindo ao app minha conta")

def info():
    global pessoas, conta
    try:
        input("digite a quantidade de pessoas: ")
        conta = float(input("digite o valor da conta: R$ "))
        pessoas = int(input("quantas pessoas sera dividida a conta: "))

        calc()

    except ValueError:
        print("algum dado está incorreto")

def calc():
    x = conta / pessoas
    
    print(f"cada pessoa deve pagar R$ {x:.2f}")

info()
    