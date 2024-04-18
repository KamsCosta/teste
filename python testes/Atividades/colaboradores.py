# Definindo os dias da semana
dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

# Perguntando quantos colaboradores irão participar da votação
num_colaboradores = int(input("Quantos colaboradores irão participar da votação? "))

# Inicializando um dicionário para armazenar os votos
votos = {dia: 0 for dia in dias_semana}

# Pedindo a preferência de cada colaborador
for i in range(num_colaboradores):
    print(f"\nColaborador {i+1}:")
    while True:
        preferencia = input("Qual é o seu dia de preferência para participar da live? ").lower()
        if preferencia in dias_semana:
            votos[preferencia] += 1
            break
        else:
            print("Por favor, escolha um dos dias da semana.")

# Encontrando o dia mais votado
dia_mais_votado = max(votos, key=votos.get)

# Exibindo o resultado
print("\nResultado da votação:")
for dia, votos_dia in votos.items():
    print(f"{dia.capitalize()}: {votos_dia} voto(s)")
print(f"\nO dia mais votado foi: {dia_mais_votado.capitalize()} com {votos[dia_mais_votado]} voto(s).")