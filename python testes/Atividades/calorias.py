quantidade_alimento = int(input("Informe quantide de alimento consumida hoje: "))
total_calorias = 0

for alimento in range(1, quantidade_alimento + 1, 1):
    calorias = int(input(f"Informe as calorias do {alimento} alimento: "))
    total_calorias = total_calorias + calorias
print(f"As calorias consumidas ao logo do dia fora {total_calorias} calorias")
