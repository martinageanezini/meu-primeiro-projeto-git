# Aluno Aprovado ou Reprovado

# Entrada de dados
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
nota3 = float(input("Digite sua nota 3: "))
nota4 = float(input("Digite sua nota 4: "))
nota5 = float(input("Digite sua nota 5: "))

# Processamento
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

# Saída de dados
print("Sua média é ", media, "\n")
if media >= 7:
    print("Você foi aprovado!")

else:
    print("Você foi reprovado!")