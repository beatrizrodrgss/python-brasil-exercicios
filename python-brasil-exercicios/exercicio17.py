# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

cobertura_por_litro = 6
tamanho_area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros_tinta = tamanho_area / cobertura_por_litro * 1.1
quantidade_latas = math.ceil(litros_tinta / 18)
preco_total_latas = quantidade_latas * 80.00
quantidade_galoes = math.ceil(litros_tinta / 3.6)
preco_total_galoes = quantidade_galoes * 25.00
quantidade_latas_mistura = int(litros_tinta / 18)
litros_restantes = litros_tinta - (quantidade_latas_mistura * 18)
quantidade_galoes_mistura = math.ceil(litros_restantes / 3.6)

preco_total_mistura = (quantidade_latas_mistura * 80.00) + (quantidade_galoes_mistura * 25.00)

print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas de tinta necessárias:", quantidade_latas)
print("Preço total das latas de tinta: R$", preco_total_latas)

print("\nSituação 2: Comprar apenas galões de 3.6 litros")
print("Quantidade de galões de tinta necessários:", quantidade_galoes)
print("Preço total dos galões de tinta: R$", preco_total_galoes)

print("\nSituação 3: Misturar latas e galões para minimizar o desperdício")
print("Quantidade de latas de tinta necessárias:", quantidade_latas_mistura)
print("Quantidade de galões de tinta necessários:", quantidade_galoes_mistura)
print("Preço total da mistura de latas e galões: R$", preco_total_mistura)
