# Função para calcular o imposto de renda
def calcular_ir(tipo_investimento, valor_resgate, dias):
    if tipo_investimento == 1:  # CDB
        if dias <= 180:
            return valor_resgate * 0.225
        elif 181 <= dias <= 360:
            return valor_resgate * 0.20
        elif 361 <= dias <= 720:
            return valor_resgate * 0.175
        else:
            return valor_resgate * 0.15
    elif tipo_investimento == 2 or tipo_investimento == 3:  # LCI ou LCA
        return 0
    else:
        return -1  # Código de investimento inválido

# Entrada do tipo de investimento, valor do resgate e número de dias investidos
tipo_investimento = int(input("Digite o tipo de investimento (1 para CDB, 2 para LCI e 3 para LCA): "))
valor_resgate = float(input("Digite o valor a ser resgatado: "))
dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))

# Verificação da validade do tipo de investimento
if tipo_investimento not in [1, 2, 3]:
    print("Tipo de investimento inválido.")
else:
    imposto_renda = calcular_ir(tipo_investimento, valor_resgate, dias_investidos)
    if imposto_renda == -1:
        print("Erro no cálculo do imposto de renda.")
    else:
        print(f"Valor do imposto de renda a ser pago: R$ {imposto_renda:.2f}")
