
from historico import Historico


class Calculadora:

    def __init__(self, historico=None):
        if historico is None:
            self._historico = Historico()
        else:
            self._historico = historico

    @property
    def historico(self):
        return self._historico

    def calcular(self, operacao, simbolo):

        resultado = operacao.executar()

        registro = (
            f"{operacao.primeiro:g} {simbolo} "
            f"{operacao.segundo:g} = {resultado:g}"
        )

        self._historico.adicionar(registro)

        return resultado
