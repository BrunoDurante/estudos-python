# Os testes foram feitos através do Python Console
class Conta:

    #atributo estatico
    endereco_banco = "Rua XPTO, numero 31"

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_ser_sacado):
        return valor_a_ser_sacado <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor {} ultrapassou o limite.".format(valor))

    def extrato(self):
        print("Saldo é de R${}".format(self.__saldo))

    def transfere(self, conta, valor):
        self.saca(valor)
        conta.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104", "Bradesco":"237"}