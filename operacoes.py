
from abc import ABC, abstractmethod


class Operacao(ABC):

    def __init__(self, primeiro, segundo):
        self._primeiro = float(primeiro)
        self._segundo = float(segundo)

    @property
    def primeiro(self):
        return self._primeiro

    @property
    def segundo(self):
        return self._segundo

    @abstractmethod
    def executar(self):
        pass


class Soma(Operacao):

    def executar(self):
        return self._primeiro + self._segundo


class Subtracao(Operacao):

    def executar(self):
        return self._primeiro - self._segundo


class Multiplicacao(Operacao):

    def executar(self):
        return self._primeiro * self._segundo


class Divisao(Operacao):

    def executar(self):
        if self._segundo == 0:
            raise ValueError("Não é possível dividir por zero.")

        return self._primeiro / self._segundo
