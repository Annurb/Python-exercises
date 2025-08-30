#Questao 7
t = int(input(("""Escolha um tipo:
1.Alcool 
2.Gasolina 
3.Diesel 
4.Fim
""")))
alcool = 0
gasolina = 0
diesel = 0
while t!=4:
    match(t):
        case 1: 
            alcool +=1
        case 2:
            gasolina +=1
        case 3:
            diesel+=1
    t = int(input())
print(f"""MUITO OBRIGADO
      Alcool: {alcool}
      Gasolina: {gasolina}
      Diesel: {diesel}""")