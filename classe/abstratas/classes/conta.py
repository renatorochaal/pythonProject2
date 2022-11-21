from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

#  criando o getters

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):  # verificando se valor sera um numerico
            raise ValueError("Saldo precisa ser númerico.")  # levantando uma exeção

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):  # verificando se valor sera um numerico
            raise ValueError("Valor do deposito precisa ser númerico.")  # levantando uma exeção

        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass
