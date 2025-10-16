#1796

q = int(input())
sat = nsat = 0
pessoas = []
pessoas = list(map(int, input().split()))
for c in range(q):
    if pessoas[c] == 1:
        nsat += 1
    else:
        sat +=1
if nsat>=sat: 
    print("N")
else:
    print("Y")