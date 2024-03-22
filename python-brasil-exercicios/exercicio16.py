# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.


cobertura_por_litro = 3
tamanho_area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
litros_tinta = tamanho_area / cobertura_por_litro

quantidade_latas = litros_tinta / 18
quantidade_latas = int(quantidade_latas) + 1 if litros_tinta % 18 != 0 else int(quantidade_latas)

preco_total = quantidade_latas * 80.00

print("Quantidade de latas de tinta necessárias:", quantidade_latas)
print("Preço total das latas de tinta: R$", preco_total)
