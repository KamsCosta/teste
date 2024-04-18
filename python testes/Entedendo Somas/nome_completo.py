#Informações do nome#

primeiro_nome = input("Informe o seu primeiro nome: ")
sobrenome = input("Informe o seu sobrenome: ")
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)

#Soma Valores#

print("Programa somador!")

valor1 = float(input("Por favor, informe o primeiro valor: "))
valor2 = float(input("Por favor, informe o segundo valor: "))

soma = valor1 + valor2

print("A soma entre os valores é {}".format(soma))
subtracao = float(valor1) - float(valor2)
print("a subtracao entre os valores é {}".format(subtracao))
divisao = float(valor1) / float(valor2)
print("A divisao entre os valores é {}".format(divisao))
multiplicacao = float(valor1) * float(valor2)
print("A multiplicacao entre os valores é {}".format(multiplicacao))

#Calculadora Patinete#

print("Esse programa calcula a velocidade média de um patinete")
distancia = input("Qual foi a distancia em metros percorrida pelo patinete? ")
tempo = input("Quantos minutos o patinete demorou para percorrer essas distância? ")
velocidade_media = float(distancia) / float(tempo)
print("O patinete atingiu uma velocidade de {0:.2f} km/h".format(velocidade_media))

#Variaveis#

print("Esse programa inverte os conteúdos de duas variáveis")
A = input("Digite o conteúdo da variável 1: ")
B = input("Digite o conteudo da variável 2: ")
troca = A
A = B 
B = troca
print("Agora que trocamos, a variável A contém {} e a variável B contém {}".format(A, B))