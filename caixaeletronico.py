opcao_de_menu = ""
valor = 0
saldo = 0
sair_operacao = False

while not sair_operacao:
    print("Escolha as opções:", opcao_de_menu)
    opcao_de_menu = input("Escolha uma opção (D para Depósito, S para Saque, V para Saldo e G para Encerrar): ").upper()
    
    if opcao_de_menu == "S" or opcao_de_menu == "D" or opcao_de_menu == "V":
        if opcao_de_menu == "V":
            print("Seu saldo é: ", saldo)
        elif opcao_de_menu == "S":
            valor = int(input("Digite o valor: "))
            if valor > saldo:
                print("Saque não permitido, saldo insuficiente.")
            else:
                saldo -= valor
                print("Saque efetuado.")
        else:
            valor = int(input("Digite o valor: "))
            saldo += valor
            print("Depósito feito.")
    elif opcao_de_menu == "G":
        sair_operacao = True
    else:
        print("Operação inválida")

print("Programa encerrado.")
