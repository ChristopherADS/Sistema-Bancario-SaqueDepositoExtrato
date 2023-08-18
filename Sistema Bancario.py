#Sistema Bancário Simples em Python

# Este é um programa de simulação de sistema bancário desenvolvido em Python. 
# A primeira versão do sistema oferece três operações principais: depósito, saque e extrato. 
# Os usuários podem realizar depósitos de valores positivos, realizar até 3 saques diários
# com limite de R$ 500,00 por saque e visualizar o extrato da conta, incluindo a listagem de 
# depósitos e saques realizados.

#Recursos:
#- Realizar depósitos com controle de saldo.
#- Realizar saques com limite máximo diário.
#- Exibir extrato com histórico de movimentações.
#- Formatação de valores no formato R$ xxx.xx.

#Esse projeto serve como um exemplo de aplicação de programação orientada a objetos em Python e 
# prática de lógica de programação. É um ponto de partida para construção de funcionalidades mais 
# avançadas e interações com usuário.

#Para utilizar o sistema, execute o código no terminal ou em um ambiente Python e siga as opções do menu.



class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')

    def saque(self, valor):
        if valor > 0 and valor <= 500 and len(self.saques) < 3:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            else:
                print('Saldo insuficiente para realizar o saque.')
        else:
            print('Saque inválido.')

    def extrato(self):
        print('Extrato:')
        if not self.depositos and not self.saques:
            print('Não foram realizadas movimentações.')
        else:
            for deposito in self.depositos:
                print(f'Depósito: R$ {deposito:.2f}')
            for saque in self.saques:
                print(f'Saque: R$ {saque:.2f}')
            print(f'Saldo atual: R$ {self.saldo:.2f}')


def main():
    conta = ContaBancaria()

    while True:
        print('\nOpções:')
        print('1. Depositar')
        print('2. Sacar')
        print('3. Extrato')
        print('4. Sair')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            valor = float(input('Digite o valor a ser depositado: '))
            conta.deposito(valor)
        elif opcao == 2:
            valor = float(input('Digite o valor a ser sacado: '))
            conta.saque(valor)
        elif opcao == 3:
            conta.extrato()
        elif opcao == 4:
            break
        else:
            print('Operação Invalida, tente novamente a operação desejada.')

if __name__ == "__main__":
    main()
