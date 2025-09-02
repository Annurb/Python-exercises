#Questão 6
a, g, ra, rg = input().split()
a = float(a)
g = float(g)
ra = float(ra)
rg = float(rg)
while not(0.01<= a <=10 and 0.01<=g<=10):
    a, g= input("Digite os preços novamente:").split()
    a = float(a)
    g = float(g)
while not(0.01 <= ra<=20 and 0.01<rg<=20):
    ra, rg = input("Digite os rendimentos novamente: ").split()
    ra  = int(ra)
    rg = int(rg)
#rendimento = km/l
# l = km/rendimento
#p/l
alcool =  ra/a
gas = rg/g
if alcool > gas:
    print("A")
else:
    print("G")
