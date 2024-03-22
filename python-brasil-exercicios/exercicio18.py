# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

tempo_download_segundos = (tamanho_arquivo_mb * 8) / velocidade_internet_mbps
tempo_download_minutos = tempo_download_segundos / 60

print("O tempo aproximado de download do arquivo é de aproximadamente", tempo_download_minutos, "minutos.")
