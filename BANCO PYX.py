import os

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
        valor = int(input("Quanto deseja depósitar? "))
        if ( valor > 0 ):
          extrato += (f"Desposito realizado no valor de R$ {valor:.2f}\n")
          saldo += valor
          os.system('clear')
        else:
            print("Valor invalido") 

    elif opcao == 2:
        # Opcao de saque
        if numero_saques < limite_saques:     
            saque = (int(input("Quanto deseja sacar? ")))
                      
            if saque > saldo or limite < saque:
                print("Operacao nao permitida, valor insuficiente ou limite diario excedido")
            else:
                saldo = saldo - saque
                extrato += (f"Saque realizado no valor de R$ {saque:.2f}\n")
                numero_saques += 1
                os.system('clear')
        else:
            print("Limite de saques excedido")
            menu = """ 
            BANCO PYX
[1] Depositar
[3] Extrato
[0] Sair

=>"""

    elif opcao == 3:
        if extrato == "":
            print("\n Nao foram realizadas movimentacoes")
        else:
            print(extrato)
            print(f"Total de saques realizados: {numero_saques}")        
            print(f"Saldo atual da conta R$ {saldo:.2f}")
            
    elif opcao == 0:
        print('''
        Obrigado por utilizar nosso servico!
        ''')
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")