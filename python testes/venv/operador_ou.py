#Uma loja concede descontos para compras com cartão de crédito com valor superior a R$100

valor_compra = float(input("Por favor, informe o toal da compra: "))
forma_pagamento = int(input("FORMA DE PAGEMENTO\n1 - CARTÃO DE CRÉDITO  \n2 - DINHEIRO \n3 Informe a forma adotada: "))

if valor_compra > 100 or forma_pagamento ==1:
    valor_compra = valor_compra * 0.9
    print("O cliente tem direito a desconto!")

print(f"O valor da compra é de {valor_compra}")