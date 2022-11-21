from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} NÃO ESTA LIGADO'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} ESTÁ CONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desliago com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False
