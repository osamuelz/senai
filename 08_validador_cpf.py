cpf = input("Digite CPF (11 dígitos): ")

d9 = [int(cpf[i]) for i in range(9)] #cria uma lista INT com 9 digitos

soma1 = 0 #variavel da multiplicação
for i in range(9): 
    soma1 += d9[i] * (10 - i)

dig1_calc = (soma1 * 10) % 11
dig1_real = int(cpf[9])

if dig1_calc == dig1_real:
    print("CPF válido (1º dígito)")
else:
    print("CPF inválido")
