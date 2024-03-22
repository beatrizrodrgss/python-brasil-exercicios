# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite a altura em metros: "))

genero = input("Digite o gênero (homem ou mulher): ")
if genero.lower() == "homem":
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem com altura", altura, "m é:", peso_ideal, "kg")
    
elif genero.lower() == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com altura", altura, "m é:", peso_ideal, "kg")

else:
    print("Gênero não reconhecido. Por favor, digite 'homem' ou 'mulher'.")
