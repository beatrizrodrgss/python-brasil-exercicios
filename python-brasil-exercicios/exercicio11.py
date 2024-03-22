# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) O produto do dobro do primeiro com metade do segundo.
# B) A soma do triplo do primeiro com o terceiro.
# C) O terceiro elevado ao cubo.

numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

resultado1 = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
resultado2 = (3 * numero_inteiro1) + numero_real
resultado3 = numero_real ** 3

print("O produto do dobro do primeiro com metade do segundo é:", resultado1)
print("A soma do triplo do primeiro com o terceiro é:", resultado2)
print("O terceiro elevado ao cubo é:", resultado3)
