
from calculadora import Calculadora
from interface import CalculadoraApp


def main():

    calculadora = Calculadora()

    app = CalculadoraApp(calculadora)

    app.executar()


if __name__ == "__main__":
    main()
