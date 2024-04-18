# Inicializando um dicionário para armazenar os votos de cada dia
votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

# Pedindo o número de colaboradores que irão participar da votação
num_colaboradores = int(input("Quantos colaboradores irão participar da votação? "))

# Loop para receber os votos de cada colaborador
for i in range(num_colaboradores):
    dia_escolhido = input(f"Informe o dia da semana de sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira ou sexta-feira): ").lower()
    
    # Verificando se o dia informado é válido
    if dia_escolhido in votos:
        # Incrementando o contador de votos para o dia escolhido
        votos[dia_escolhido] += 1
    else:
        print("Dia inválido. Por favor, escolha um dos dias da semana mencionados.")

# Encontrando o dia com mais votos
dia_vencedor = max(votos, key=votos.get)

# Exibindo o resultado
print(f"\nO dia escolhido pelos colaboradores para a live é: {dia_vencedor.capitalize()}, com um total de {votos[dia_vencedor]} votos.")
