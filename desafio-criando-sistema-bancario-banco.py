class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= ContaBancaria.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

class SistemaBancario:
    def __init__(self):
        self.conta = ContaBancaria()

    def exibir_menu(self):
        menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
        while True:
            opcao = input(menu)

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                self.conta.depositar(valor)

            elif opcao == "s":
                valor = float(input("Informe o valor do saque: "))
                self.conta.sacar(valor)

            elif opcao == "e":
                self.conta.exibir_extrato()

            elif opcao == "q":
                print("Obrigado por utilizar o sistema bancário!")
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.exibir_menu()
