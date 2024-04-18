# Função para calcular o valor da parcela
def calcular_valor_parcela(total_divida, num_parcelas, juros):
    valor_juros = total_divida * juros / 100
    total_com_juros = total_divida + valor_juros
    valor_parcela = total_com_juros / num_parcelas
    return valor_juros, total_com_juros, valor_parcela

# Função para exibir a tabela de parcelamento
def exibir_tabela(total_divida):
    for parcelas, juros in tabela_parcelas_juros.items():
        valor_juros, total_com_juros, valor_parcela = calcular_valor_parcela(total_divida, parcelas, juros)
        print(f"Total: R$ {total_com_juros:.2f} Juros: R$ {valor_juros:.2f} Número de parcelas: {parcelas} Valor da Parcela: R$ {valor_parcela:.2f}")

# Tabela de parcelas e juros
tabela_parcelas_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

# Entrada do valor da dívida
divida = float(input("Digite o valor da dívida: "))

# Exibição da tabela de parcelamento
exibir_tabela(divida)
