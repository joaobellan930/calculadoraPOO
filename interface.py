
import tkinter as tk
from tkinter import messagebox

from operacoes import (
    Soma,
    Subtracao,
    Multiplicacao,
    Divisao
)


class CalculadoraApp:

    def __init__(self, calculadora):

        self.calculadora = calculadora

        self.janela = tk.Tk()
        self.janela.title("Calculadora POO")
        self.janela.geometry("440x570")
        self.janela.minsize(400, 520)
        self.janela.configure(bg="#eef2f7")

        self.criar_componentes()
        self.atualizar_historico()

    def criar_componentes(self):

        principal = tk.Frame(
            self.janela,
            padx=22,
            pady=20,
            bg="#eef2f7"
        )

        principal.pack(fill="both", expand=True)

        titulo = tk.Label(
            principal,
            text="CALCULADORA POO",
            font=("Arial", 19, "bold"),
            bg="#eef2f7",
            fg="#17324d"
        )

        titulo.pack(pady=(0, 18))

        tk.Label(
            principal,
            text="Primeiro número",
            bg="#eef2f7"
        ).pack(anchor="w")

        self.entrada1 = tk.Entry(
            principal,
            font=("Arial", 13)
        )

        self.entrada1.pack(
            fill="x",
            ipady=7,
            pady=(4, 12)
        )

        tk.Label(
            principal,
            text="Segundo número",
            bg="#eef2f7"
        ).pack(anchor="w")

        self.entrada2 = tk.Entry(
            principal,
            font=("Arial", 13)
        )

        self.entrada2.pack(
            fill="x",
            ipady=7,
            pady=(4, 14)
        )

        botoes = tk.Frame(
            principal,
            bg="#eef2f7"
        )

        botoes.pack(fill="x")

        configuracoes = [
            ("Somar +", Soma, "+"),
            ("Subtrair −", Subtracao, "-"),
            ("Multiplicar ×", Multiplicacao, "*"),
            ("Dividir ÷", Divisao, "/")
        ]

        for indice, (texto, classe, simbolo) in enumerate(configuracoes):

            botao = tk.Button(
                botoes,
                text=texto,
                font=("Arial", 11, "bold"),
                bg="#d9e7f5",
                fg="#17324d",
                relief="flat",
                height=2,
                command=lambda c=classe, s=simbolo:
                    self.calcular(c, s)
            )

            botao.grid(
                row=indice // 2,
                column=indice % 2,
                sticky="nsew",
                padx=4,
                pady=4
            )

        botoes.columnconfigure(0, weight=1)
        botoes.columnconfigure(1, weight=1)

        self.resultado_var = tk.StringVar(
            value="Resultado: —"
        )

        tk.Label(
            principal,
            textvariable=self.resultado_var,
            font=("Arial", 15, "bold"),
            bg="#eef2f7",
            fg="#17633a"
        ).pack(pady=16)

        acoes = tk.Frame(
            principal,
            bg="#eef2f7"
        )

        acoes.pack(fill="x", pady=(0, 14))

        tk.Button(
            acoes,
            text="Limpar campos",
            command=self.limpar_campos,
            bg="#e2e6eb",
            relief="flat"
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=3,
            ipady=5
        )

        tk.Button(
            acoes,
            text="Limpar histórico",
            command=self.limpar_historico,
            bg="#f3dddd",
            relief="flat"
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=3,
            ipady=5
        )

        tk.Label(
            principal,
            text="Histórico de cálculos",
            font=("Arial", 11, "bold"),
            bg="#eef2f7"
        ).pack(anchor="w")

        area = tk.Frame(principal)
        area.pack(fill="both", expand=True, pady=(6, 0))

        self.lista_historico = tk.Listbox(
            area,
            height=9,
            font=("Consolas", 10)
        )

        barra = tk.Scrollbar(
            area,
            command=self.lista_historico.yview
        )

        self.lista_historico.configure(
            yscrollcommand=barra.set
        )

        self.lista_historico.pack(
            side="left",
            fill="both",
            expand=True
        )

        barra.pack(side="right", fill="y")

    def calcular(self, classe_operacao, simbolo):

        try:
            texto1 = self.entrada1.get().strip().replace(",", ".")
            texto2 = self.entrada2.get().strip().replace(",", ".")

            if not texto1 or not texto2:
                raise ValueError(
                    "Preencha os dois campos com números."
                )

            primeiro = float(texto1)
            segundo = float(texto2)

            operacao = classe_operacao(
                primeiro,
                segundo
            )

            resultado = self.calculadora.calcular(
                operacao,
                simbolo
            )

            self.resultado_var.set(
                f"Resultado: {resultado:g}"
            )

            self.atualizar_historico()

        except ValueError as erro:

            messagebox.showerror(
                "Dados inválidos",
                str(erro)
            )

    def atualizar_historico(self):

        self.lista_historico.delete(0, tk.END)

        for registro in self.calculadora.historico.listar():
            self.lista_historico.insert(
                tk.END,
                registro
            )

    def limpar_campos(self):

        self.entrada1.delete(0, tk.END)
        self.entrada2.delete(0, tk.END)

        self.resultado_var.set("Resultado: —")

        self.entrada1.focus_set()

    def limpar_historico(self):

        self.calculadora.historico.limpar()
        self.atualizar_historico()

    def executar(self):

        self.janela.mainloop()
