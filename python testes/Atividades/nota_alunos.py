#Solicitando os dados do aluno

email_aluno = input("Informe o e-mail do ano: ")
nota_semestral = input("Informe a nota semestral do aluno: ")

#Convertendo a nota de forma float
nota_semestral = float(nota_semestral)

#Realizando teste lógico
if nota_semestral > 8.5:
    print(f"ENVIADO E-MAIL PARA {email_aluno}")
