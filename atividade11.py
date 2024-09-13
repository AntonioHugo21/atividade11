# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("digite a idade"))
# Criança (0-12 anos)
if(idade<=12):
    print("criança")
# Adolescente (13-17 anos)
elif(idade>=13) and (idade<=17):
    print("adolescente")
# Adulto (18-59 anos)
elif(idade>=18) and (idade<=59):
    print("adulto")
# Idoso (60 anos ou mais)
elif(idade>=60):
    print("idoso")