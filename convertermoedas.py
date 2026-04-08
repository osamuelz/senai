import os
#Criando as funções
#Criando a função que exibi o menu
def exibir_menu():
    print("=== Conversor de Moedas ===")
    print("[1] - Converter DOLAR -> REAL")
    print("[2] - Converter REAL -> DOLAR")
    print("[3] - Sair")
 
#Criando a funcao limpar tela
def limpar_tela():
    os.system("cls")
 
#Função Converter de dolar para real
def converter_dolar_para_real(quantia_dolar, cotacao):
    total_reais = quantia_dolar * cotacao
    return total_reais
 
#Função Converter de Real para Dolar
def converter_real_para_dolar(quantia_real, cotacao):
    total_dolares = quantia_real / cotacao
    return total_dolares
 
#Função Sair
def sair():
   exit()
 
#Criando a função main - principal
def main():
    limpar_tela()
    #Chamar a funcao exibir_menu
    exibir_menu()
 
    # Solicitando a opção do usuário
    opcao = int(input("Escolha uma opção:"))
 
    if(opcao == 1):
        quantia_dolar = float(input("Informe a quantia de dolares:"))
        cotacao = float(input("Informe a cotação:").replace(",", "."))
        resultado = converter_dolar_para_real(quantia_dolar, cotacao)
        print(f"O total da conversão é: R${resultado}")
   
    elif(opcao == 2):
        quantia_reais = float(input("Informe a quantia de reais:"))
        cotacao = float(input("Informe a cotação:").replace(",","."))
        resultado = converter_real_para_dolar(quantia_reais, cotacao)
        print(f"O total da conversão é: ${resultado}")
    elif(opcao == 3):
        sair()
       
#Chamando a função principal do programa
main()