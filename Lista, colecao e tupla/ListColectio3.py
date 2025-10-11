#Questão 1
futebol = set()
basquete = set()
natacao = set()
volei = set()
numaluno = numfut = numbas = numnat = numvol = 0
relfut = relbas = relnat = relvol = 0
while True:
    modalidade = int(input("""
    Digite a modalidade: 
    1 - Futebol
    2 - Basquete
    3 - Natação
    4 - Vôlei
    5 - Sair              
    """))
    if modalidade == 5:
        break
    a = input("Digite o nome do aluno: ")
    numaluno +=1
    match(modalidade):
        case 1:
            futebol.add(a)
            numfut +=1
            relfut = numfut/numaluno
        case 2:
            basquete.add(a)
            numbas +=1
            relbas = numbas/numaluno
        case 3:
            natacao.add(a)
            numnat +=1
            relnat = numnat/numaluno
        case 4:
            volei.add(a)
            numvol +=1
            relvol = numvol/numaluno
    print(f"""Relação de alunos por modalidade
Futebol: {relfut:.2f} 
Basquete: {relbas:.2f}
Natação: {relnat:.2f}
Vôlei: {relvol:.2f}""")
    i1 = futebol.intersection(basquete)
    i2 = futebol.intersection(natacao)
    i3 = futebol.intersection(volei)
    i4 = basquete.intersection(natacao)
    i5 = basquete.intersection(volei)
    i6 = natacao.intersection(volei)
    uniao= i1.union(i2, i3, i4, i5, i6)
    print(f"Alunos que possuem direito ao desconto: {uniao}")
    print(f"""Número de alunos por modalidade:
Futebol: {(numfut)}
Natação: {(numnat)}
Vôlei: {(numvol)}
Basquete: {(numbas)}

Número total de alunos: {numaluno}  """)

#Questão 2
numempresa = numcliente =  numempresa1 = numempresa2 = rel1 = rel2 = 0
empresa1 = set()
empresa2 = set()
while True:
    modalidade = int(input("""
    Digite a empresa: 
    1 - Empresa 1
    2 - Empresa 2  
    3 - Sair        
    """))
    if modalidade == 3:
        break
    a = input("Digite o nome do cliente: ")
    numcliente +=1
    match(modalidade):
        case 1:
            empresa1.add(a)
            numempresa1 +=1
            rel1 = numempresa1/numcliente
        case 2:
            empresa2.add(a)
            numempresa2 +=1
            rel2 = numempresa2/numcliente
    print(f"""Relação de clientes por empresa:
    Empresa 1: {rel1:.2f} 
    Empresa 2: {rel2:.2f}""")
    i = empresa1.intersection(empresa2)
    if len(i) == 0:
        print("Não existem clientes nas 2 empresas")
    else:
        print("Cientes cadastrados nas 2 empresas: ", ", ".join(i))
    apenas1 = empresa1.difference(empresa2)
    apenas2 = empresa2.difference(empresa1)
    if len(apenas1) == 0:
        apenas1 = 0
    if len(apenas2) == 0:
        apenas2 = 0
    print(f"""Número de clientes da empresa 1: {len(empresa1)}
Número de clientes da empresa 2: {len(empresa2)}
Clientes pertencentes a apenas a empresa 1: {apenas1} 
Clientes pertencentes a apenas a empresa 2: {apenas2} 
Número total de clientes: {numcliente}
""")
    
#Questão 3
lista = []
conjunto = set()
n = int(input())
lista = list(map(int, input().split()))
conjuntoin = set(lista)
for c in range(n):
    conjunto.add(c+1)
diferenca = conjunto.difference(conjuntoin)
print(', '.join(map(str, diferenca)))

#Questão 4
lista = []
lista = list(map(int, input().split()))
conjunto = set(lista)
print(f"Há {len(conjunto)} valor(es) distinto(s)")