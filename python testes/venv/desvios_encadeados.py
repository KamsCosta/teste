#Faixas de bônus
#> 1000 3gb
#> 500 1,5gb
#> 200 500m 
#< 200 nenhum bônus

pontos = int(input("Informe a quantidade de pontos do cliente: "))
if pontos >= 1000:
    print("O cliente recebe 3gb adicionais! ")
elif pontos > 500:
    print("O cliente rece 1,5gb adicionais! ")
elif pontos > 200:
    print("O cliente recebe 500mb adicionais! ")
else:
    print("O cliente não recebe dados adicionais! ")

