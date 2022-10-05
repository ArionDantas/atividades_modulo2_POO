"""
M02W01E02

Problema
Utilizando a classe implementada no exercício anterior, crie a classe Triangulo, cujos atributos deverão ser três pontos distintos. Considere que os
pontos não sejam colineares. A classe deverá possuir um método que calcule
o perímetro de um triângulo.
As entradas deverão ser seis numeros reais, representando de dois em dois as
coordenadas dos três vértices do triângulo.
A saída deverá ser o perímetro do triângulo, represetada por um número
real com duas casas decimais apenas.
Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste!
----------------------------------------
Exemplo de Entrada  |  Exemplo de Saida
----------------------------------------
0                   |   12.00
0                   |
0                   |
3                   |
4                   |
0                   |
----------------------------------------
0                   |   24.14
0                   |
10                  |
0                   |
5                   |
5                   |
----------------------------------------
"""


import math

class Triangulo:
  def __init__(self, ax, ay, bx, by, cx, cy):
    self.ax = ax
    self.ay = ay
    self.bx = bx
    self.by = by
    self.cx = cx
    self.cy = cy
    self.d_ab = d_ab = math.sqrt(math.pow((ax1 - bx2), 2) + math.pow((ay1 - by2), 2))
    self.d_ac = d_ac = math.sqrt(math.pow((ax1 - cx3), 2) + math.pow((ay1 - cy3), 2))
    self.d_cb = d_cb = math.sqrt(math.pow((cx3 - bx2), 2) + math.pow((cy3 - by2), 2))
    self.resultado = d_ab + d_ac + d_cb

  def __str__(self):
    return f"{self.resultado:.2f}"

ax1 = int(input())
ay1 = int(input())
bx2 = int(input())
by2 = int(input())
cx3 = int(input())
cy3 = int(input())

triangulo = Triangulo(ax1, ay1 , bx2, by2, cx3, cy3)
print(triangulo)