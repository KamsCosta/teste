print("Esse programa calcula a velocidade média de um patinete")
distancia = input("Qual foi a distancia em metros percorrida pelo patinete? ")
tempo = input(
    "Quantos minutos o patinete demorou para percorrer essas distância? ")
velocidade_media = float(distancia) / float(tempo)
print("O patinete atingiu uma velocidade de {}m/min".format(velocidade_media))
