"""
M02W01E04

Problema
Tendo feito o exercício P190702, seu dever agora é aprimorá-lo. No método
construtor, você deverá verificar se os pontos dados realmente formam um
triângulo. Caso os pontos sejam colineares, o programa deverá ser abortado
infomando a mensagem "ERRO! Os pontos dados nao formam um triangulo",(Dica: é possível realizar essa verificação utilizando geometria analítica,
pesquise!).

Caso os pontos formem um triângulo, então o programa deverá informar a
mensagem "Os pontos dados formam um triangulo <tipo do triângulo>"Ex:
"Os pontos dados formam um triangulo equilatero". Os tipos são equilátero,
isóceles ou escaleno.
Logo após isso, o programa receberá UM número inteiro sendo 1 para
calcular o perímetro ou 2 para calcular a área do triângulo. Considere que
não haja entradas diferentes de 1 ou 2.
Incialmemte o programa receberá seis números reais repesentando, duas as
duas, as coordenadas dos vértices do triângulo. O programa fará a verificação
de existência, e só após o programa receberá o número inteiro representando
a opção que o usuário quer calcular.
Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.

-------------------------------------------------------------
Exemplo de Entrada     |   Exemplo de Saida
-------------------------------------------------------------
0                      |    ERRO! Os pontos dados nao formam
0                      |    um triangulo
1                      | 
1                      | 
2                      |
2                      |     
1                      |     
-------------------------------------------------------------
0                      |    Os pontos dados formam um
0                      |    triangulo isoceles
10                     |    25.00
0                      | 
5                      | 
5                      | 
2                      | 
-------------------------------------------------------------
"""

import math


class Colinear:
  def __init__(self, ax1, ay1, bx2, by2, cx3, cy3):
    self.ax1 = ax1
    self.ay1 = ay1
    self.bx2 = bx2
    self.by2 = by2
    self.cx3 = cx3
    self.cy3 = cy3
    self.resultado = ((ax1 * bx2 * 1) + (ay1 * 1 * cx3) + (1 * bx2 * cy3) + (-(cx3 * by2 * 1)) + (-(cy3 * 1 * ax1)) + (-(1 * bx2 * ay1))) # 

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
    self.area = 0

  def descobrirArea(self, teste):
      if teste < 0:
        teste = -(teste)
      else:
        teste = teste

      area = teste / 2

      print(f"{area:.2f}")
    

ax1 = float(input())
ay1 = float(input())
bx2 = float(input())
by2 = float(input())
cx3 = float(input())
cy3 = float(input())
escolha = int(input())

verificar_colinear = Colinear(ax1, ay1 , bx2, by2, cx3, cy3)
triangulo = Triangulo(ax1, ay1 , bx2, by2, cx3, cy3)

while True:
  if verificar_colinear.resultado == 0:
    print(f"ERRO! Os pontos dados nao formam um triangulo")
    break
  elif triangulo.d_ab != triangulo.d_ac != triangulo.d_cb:
    print(f"Os pontos dados formam um triangulo escaleno")
  elif triangulo.d_ab == triangulo.d_ac == triangulo.d_cb:
    print(f"Os pontos dados formam um triangulo equilatero")
  else:
    print(f"Os pontos dados formam um triangulo isoceles")

  if escolha == 1:
    print(f"{triangulo.resultado:.2f}")
  elif escolha == 2:
    triangulo.descobrirArea(verificar_colinear.resultado)
  break