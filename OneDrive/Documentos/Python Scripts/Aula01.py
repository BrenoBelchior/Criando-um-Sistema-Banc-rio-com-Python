class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.saques_diarios = 0
        self.limite_saques_diarios = 3

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido. Tente novamente.")

    def sacar(self, valor):
        if valor > self.limite_saque:
            print(f"Valor de saque excede o limite de R${self.limite_saque:.2f}.")
        elif self.saques_diarios >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R${valor:.2f}")
            self.saques_diarios += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def mostrar_extrato(self):
        print("\nExtrato:")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")


def menu():
    banco = Banco()
    while True:
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor para depósito: "))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: "))
            banco.sacar(valor)
        elif opcao == '3':
            banco.mostrar_extrato()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()