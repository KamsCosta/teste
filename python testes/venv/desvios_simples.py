#Pedir que o usuário digite o nome do funcionário
nome = input("Informe o nome do funcionário: ")
#Pedir que o usuário digite o salário do funcionário
salario = float(input("Informe o salário do funcionário: "))
#Caso o salário seja negativo, alertaro usuário
if salario < 0:
    salario = salario * - 1
    print("Atenção, foi informado um salário negativo!")
#Exibir o salário armazenado
print(f"O funcionário {nome} tem um salário de R$:{salario}")