
class Historico:

    def __init__(self):
        self._registros = []

    def adicionar(self, registro):
        self._registros.append(str(registro))

    def listar(self):
        return self._registros.copy()

    def limpar(self):
        self._registros.clear()
