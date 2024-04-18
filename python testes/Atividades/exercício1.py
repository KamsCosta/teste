# Verificar se o batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar que o usuário informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE. A partir disso o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, de acordo com o site Tua Saude (http://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20de%20idade,idosos%3A250%20a%2060%20bpm.):

#IDADE BPM
#Até 2 anos 120 a 140
#De 8 anos até 17 anos 80 a 100
#Adulto sedentário de 70 a 80
#Idoso 50 a 60

print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
idade = int(input("Por favor, informe a sua idade: "))
bpm = int(input("Por favor, informe a sua bpm: "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequencia cardiaca inadequada")
    else:
        print("Frequencia cardiaca inadequada")
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
elif idade >= 18 and idade <= 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Frequencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
else:
    print("Não existem dados para a idade indicada")