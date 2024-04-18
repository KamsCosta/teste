#Solicitar os dados do cliente

valor_compra = input("Informe o valor da compra realizada: ")
cupom = input("Digite o cupom de desconto: ")

#Realizando o teste lógico
if cupom.upper() == "NIVER10":
    #cálculo de 10% de desconto
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("CUPOM INVÁLIDO")
#Exibindo o valor final da compra
print(f"O valor final da compra é {valor_final}")
