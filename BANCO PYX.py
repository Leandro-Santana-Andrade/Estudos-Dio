import os # Adicionado para utilizar a opção de limpar menu
menu = """ 
            BANCO PYX
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
  
    opcao = int(input(menu))

    if opcao == 1:
        # Opcao de deposito
        valor = float(input("Quanto deseja depósitar? "))
        if ( valor > 0 ):
          extrato += (f"Desposito realizado no valor de R$ {valor:.2f}\n")
          saldo += valor
          os.system('clear')
        else:
            print("Valor invalido, tente novamente!") 

    elif opcao == 2:
        # Opcao de saque
        if numero_saques < limite_saques:     
            saque = (float(input("Quanto deseja sacar? ")))
             # Valida se possui saldo e se esta dentro do limite diario         
            if saque > saldo or limite < saque:
                print("Operacao nao permitida, valor insuficiente ou limite diario excedido")
                print(f"Limite diario R$ {limite}")
                print(f"Saldo em conta R$ {saldo:.2f}")
            else:
                saldo = saldo - saque
                extrato += (f"Saque realizado no valor de R$ {saque:.2f}\n")
                numero_saques += 1
                os.system('clear')
        else:
            # Informa que nao ha mais limite para saque e eliminar opção de sacar do menu
            print("Limite de saques excedido")
            menu = """ 
            BANCO PYX
[1] Depositar
[3] Extrato
[0] Sair

=>"""
    elif opcao == 3:
    # Opção de extrato
        if extrato == "":
            print("\n Nao foram realizadas movimentacoes")
        else:
            print(extrato)
            print(f"Total de saques realizados: {numero_saques}")        
            print(f"Saldo atual da conta R$ {saldo:.2f}")
            
    elif opcao == 0:
    # Opção de sair da aplicação
        print('''
        Obrigado por utilizar nosso servico!
        ''')
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
