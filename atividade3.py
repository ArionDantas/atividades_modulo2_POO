"""
Problema

Implemente a classe Carro que possua os atributos velocidade media, consumo(dada em km/litro), capacidade do tanque de combustivel e quantidade
atual de combustivel. Além disso, essa classe também deverá possuir alguns
métodos:

1. O método Viajar, que recebe a quantidade de quilômetros como parâmetro.
2. O método Abastecer, que recebe a quantidade de combustivel a ser
abastecida
3. O método Completar, que enche o tanque de combustivel até o limite
da capacidade.

Seu programa deve começar lendo os atributos do carro: velocidade média, consumo e capacidade do tanque, respectivamente. Considere que o
carro começa com o tanque cheio.
Após ler esses valores e criar um Carro, seu programa receberá comandos
que serão associados com cada método de carro: Ao ler "Viaja", a próxima
linha será um número real que representa a quantidade de km que serão percorridos, e portanto, deve-se chamar o método Viajar e usar a quantidade
de km lida como argumento do método. Ao ler "Abastece", a próxima linha
será um número real que representa quantos litros de combustivel devem ser
abastecidos, e portanto, deve-se chamar o método Abastecer e usar a quantidade de litros lida como argumento do método.Por fim, ao ler "Completa",
seu programa deve chamar o método Completar, que não possui argumentos.
Seu programa deve receber comandos até que, ao invés de receber um dos
três comandos listados acima, receba o comando "Encerra", que deve encerrar
o programa.
As saídas possíveis são três:

1. Ao chamar o método Viajar, deve-se imprimir "O carro andou KM
km em H horas e gastou L litros de combustivel. O carro agora possui
Latual litros de combustivel."substituindo os valores em maiúsculo pelos
valores apropriados.
2. Ao chamar o método Abastecer, deve-se imprimir "O carro foi abastecido com L litros. O tanque agora esta com Latual litros de combustivel."caso o tanque não tenha sido abastecido até sua capacidade
máxima. Caso o tanque tenha sido abastecido até sua capacidade máxima, deve-se imprimir "O carro foi abastecido com L litros e esta com
o tanque cheio!".
3. Ao chamar o método Completar, também deve-se imprimir "O carro
foi abastecido com L litros e esta com o tanque cheio!".
OBS1: Considere que o o comando "Viaja"nunca enviará um número de
KMs maior do que o máximo que o carro consegue percorrer com o combustivel atual. Além disso, ao receber o comando "Abastece"e receber um número
de litros de combustivel que faça com que o tanque transborde, considere que
o número passado foi exatamente o necessário para completar o tanque.

OBS2: Considere que não há diferença entre letras maiúsculas ou minúsuculas.
Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
-----------------------------------------------------------------------------------------------
Exemplo de Entrada     |   Exemplo de Saida
-----------------------------------------------------------------------------------------------
60                     |    O carro andou 900.00 km em 15.00 horas e gastou 75.00 litros de
12                     |    combustivel. O carro agora possui 25.00 litros de combustivel.
100                    |    O carro foi abastecido com 40.00 litros. O tanque agora esta
Viaja                  |    com 65.00 litros de combustivel.
900                    |    O carro foi abastecido com 35.00 litros e esta com o tanque cheio!
abastece               | 
40                     | 
Completa               | 
ENCERRA                | 
-----------------------------------------------------------------------------------------------
"""
class Carro:
    # consumo = km / l
    def __init__(self, velocidadeMedia, consumo, capacidadeTanque):
        self.velocidadeMedia = velocidadeMedia
        self.consumo = consumo
        self.capacidadeTanque = capacidadeTanque
        self.quantCombAtual= capacidadeTanque
        self.velocidade_media = 0

    def viajar(self, kmPecorridos):
        maxKm = self.consumo * self.capacidadeTanque # máximo de km que o carro pode andar
        if kmPecorridos < maxKm:
            self.velocidade_media = (kmPecorridos / self.velocidadeMedia) #tempo de viajem
            comb_gasto = kmPecorridos / self.consumo # combustível gasto
            self.quantCombAtual = self.quantCombAtual - comb_gasto
        else:
            diferencaKm = kmPecorridos - maxKm
            kmPecorridos = kmPecorridos - diferencaKm
            self.velocidade_media = (kmPecorridos / self.velocidadeMedia) #tempo de viajem
            comb_gasto = kmPecorridos / self.consumo # combustível gasto
            self.quantCombAtual = self.capacidadeTanque - comb_gasto

            if self.quantCombAtual < 0:
                for x in range(self.quantCombAtual, 0):
                    self.quantCombAtual += 1

        print(f"O carro andou {kmPecorridos:.2f} km em {self.velocidade_media:.2f} horas e gastou {comb_gasto:.2f} litros de combustivel. O carro agora possui {self.quantCombAtual:.2f} litros de combustivel.")

    def abastecer(self, litrosAbastecidos):
        self.quantCombAtual += litrosAbastecidos
        if self.quantCombAtual > self.capacidadeTanque:
            diferenca = self.quantCombAtual - self.capacidadeTanque
            self.quantCombAtual -= diferenca

        print(
            f"O carro foi abastecido com {litrosAbastecidos:.2f} litros. O tanque agora esta com {self.quantCombAtual:.2f} litros de combustivel.")

    def completar(self):
        completar = self.capacidadeTanque - self.quantCombAtual
        self.quantCombAtual += completar
        print(f"O carro foi abastecido com {completar:.2f} litros e esta com o tanque cheio!")


# programa = " "
vm = int(input())  # km / l
consumo = int(input())
capTanque = int(input())
carro1 = Carro(vm, consumo, capTanque)

# while programa != "encerrar":
while True:

    try:
        programa = input()
        programa = programa.lower()

        if programa == "encerrar":
            break
        elif programa == "viaja":
            km = int(input())
            carro1.viajar(km)
        elif programa == "abastece":
            quantidadeCosbutivel = int(input())
            carro1.abastecer(quantidadeCosbutivel)
        elif programa == "completa":
            carro1.completar()

    except EOFError:
        break