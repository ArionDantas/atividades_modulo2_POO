"""
M02W01E01

Problema
Faça um programa que calcule a distância entre dois pontos. Para isso implemente a classe Ponto, cujos atributos deverão ser as coordenadas x e y.
A classe deverá possuir o método construtor e um método que calcule a distância entre dois pontos.
As entradas deverão ser quatro números reais represenando respectivamente
as coordenadas x1 e y1 do primeiro ponto e as coordenadas x2 e y2 do segundo ponto.
A saída deverá ser um número real, com duas casas decimais apenas, representando a distância entre os dois pontos.
Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
------------------------------------
Exemplo de Entrada  |  Exemplo de Saida
------------------------------------
2                   |   5.50
0                   |
2                   |
5.5                 |
------------------------------------
0                   |   15.00
9                   |
12                  |
0                   |
------------------------------------
"""

import math

class Ponto:
    def __init__(self, ax, ay, bx, by):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by

    def resultado(self):
        resultado = math.sqrt(math.pow((ax - bx), 2) + math.pow((ay - by), 2))
        print(f"{resultado:.2f}")

ax = float(input())
ay = float(input())
bx = float(input())
by = float(input())

ponto = Ponto(ax, ay, bx, by)
ponto.resultado()