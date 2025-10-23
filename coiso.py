# Capacidade máxima do novo bondinho
capacidade = 30

# Número fixo de professores
professores = 8

# Solicita os dados ao usuário
alunos = int(input("Digite o número de alunos: "))
monitores = int(input("Digite o número de monitores: "))

# Calcula o total de pessoas
total_pessoas = alunos + monitores + professores

# Verifica se o total cabe em uma viagem
if total_pessoas <= capacidade:
    print(f"✅ É possível levar todos em uma viagem! Total de pessoas: {total_pessoas}.")
else:
    excedente = total_pessoas - capacidade
    print(f"🚫 Não é possível levar todos em uma viagem.")
    print(f"Total de pessoas: {total_pessoas}. Excedeu o limite em {excedente} pessoa(s).")
