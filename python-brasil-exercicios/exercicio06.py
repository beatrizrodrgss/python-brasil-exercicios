# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print("A área do círculo com raio", raio, "é:", area)
