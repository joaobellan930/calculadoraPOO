# Calculadora POO

## Sobre o projeto

Este projeto é uma calculadora desenvolvida em Python utilizando Programação Orientada a Objetos (POO) e a biblioteca Tkinter para criar a interface gráfica.

A calculadora permite realizar operações matemáticas básicas de forma simples e prática.

## Funcionalidades

- Soma de dois números.
- Subtração de dois números.
- Multiplicação de dois números.
- Divisão de dois números.
- Exibição do resultado na tela.
- Registro das operações em um histórico.
- Opção para limpar o histórico.
- Tratamento de erros, como divisão por zero e valores inválidos.

## Tecnologias utilizadas

- Python
- Tkinter
- Programação Orientada a Objetos (POO)
- PyInstaller

## Organização dos arquivos

- `main.py`: inicia o programa.
- `interface.py`: contém a interface gráfica.
- `calculadora.py`: controla os cálculos.
- `operacoes.py`: contém as operações matemáticas.
- `historico.py`: armazena o histórico dos cálculos.
- `testes.py`: contém os testes do programa.

## Como executar o projeto

1. Instale o Python no computador.
2. Abra a pasta do projeto.
3. Abra o terminal nessa pasta.
4. Execute o comando:

```bash
python main.py
```

## Como gerar o executável

Para gerar o arquivo `.exe` no Windows:

1. Instale o PyInstaller:

```bash
python -m pip install pyinstaller
```

2. Execute o comando:

```bash
python -m PyInstaller --onefile --windowed --name CalculadoraPOO main.py
```

3. Após finalizar, o executável estará na pasta `dist`, com o nome `CalculadoraPOO.exe`.

## Objetivo

O objetivo deste projeto é aplicar os conceitos de Programação Orientada a Objetos em Python, utilizando classes, herança, encapsulamento, abstração e polimorfismo.

---

**Projeto acadêmico de Programação Orientada a Objetos.**
