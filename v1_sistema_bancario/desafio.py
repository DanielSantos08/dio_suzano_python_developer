# Sistema Bancário - Versão 1.0
# Desafio DIO - Suzano Python

# Variáveis para armazenar o estado da conta
saldo = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500

def exibir_menu():
    """Exibe o menu de opções do sistema bancário"""
    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    ======================================
    => """
    return input(menu)

def depositar(valor, saldo, extrato):
    """
    Realiza operação de depósito
    Args:
        valor: Valor a ser depositado
        saldo: Saldo atual da conta
        extrato: Histórico de transações
    Returns:
        tuple: (novo_saldo, novo_extrato)
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\n=== Depósito realizado com sucesso! ===")
        print(f"Valor depositado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar(valor, saldo, extrato, numero_saques, limite_saques, limite_valor):
    """
    Realiza operação de saque
    Args:
        valor: Valor a ser sacado
        saldo: Saldo atual da conta
        extrato: Histórico de transações
        numero_saques: Número de saques realizados hoje
        limite_saques: Limite diário de saques
        limite_valor: Valor máximo por saque
    Returns:
        tuple: (novo_saldo, novo_extrato, novo_numero_saques)
    """
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_valor
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite_valor:.2f}. @@@")

    elif excedeu_saques:
        print(f"\n@@@ Operação falhou! Número máximo de saques ({limite_saques}) excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n=== Saque realizado com sucesso! ===")
        print(f"Valor sacado: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print(f"Saques restantes hoje: {limite_saques - numero_saques}")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    """
    Exibe o extrato da conta
    Args:
        saldo: Saldo atual da conta
        extrato: Histórico de transações
    """
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    """Função principal do sistema bancário"""
    global saldo, extrato, numero_saques

    print("=== Bem-vindo ao Sistema Bancário ===")

    while True:
        opcao = exibir_menu()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: R$ "))
                saldo, extrato = depositar(valor, saldo, extrato)
            except ValueError:
                print("\n@@@ Valor inválido! Digite apenas números. @@@")

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: R$ "))
                saldo, extrato, numero_saques = sacar(
                    valor, saldo, extrato, numero_saques,
                    LIMITE_SAQUES, LIMITE_VALOR_SAQUE
                )
            except ValueError:
                print("\n@@@ Valor inválido! Digite apenas números. @@@")

        elif opcao == "e":
            exibir_extrato(saldo, extrato)

        elif opcao == "q":
            print("\n=== Obrigado por usar nosso sistema! ===")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()