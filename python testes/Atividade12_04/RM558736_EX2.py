# Função para calcular o preço final com desconto ou acréscimo
def calcular_preco_final(preco, desconto=0, acrescimo=0):
    preco_final = preco * (1 - desconto/100) * (1 + acrescimo/100)
    return preco_final

# Função para calcular o valor da parcela
def calcular_valor_parcela(preco_final, num_parcelas):
    valor_parcela = preco_final / num_parcelas
    return valor_parcela

# Função para exibir a tabela de parcelamento
def exibir_tabela(preco):
    print(f"O preço final à vista com desconto de 20% é: R${calcular_preco_final(preco, desconto=20):.2f}")

    for parcelas in range(6, 61, 6):
        acrescimo = parcelas * 3
        preco_final = calcular_preco_final(preco, acrescimo=acrescimo)
        valor_parcela = calcular_valor_parcela(preco_final, parcelas)
        print(f"O preço final parcelado em {parcelas}x é de R${preco_final:.2f} com parcelas de R${valor_parcela:.2f}")

# Entrada do preço do carro
preco_carro = float(input("Digite o preço do carro: "))

# Exibição da tabela de parcelamento
exibir_tabela(preco_carro)