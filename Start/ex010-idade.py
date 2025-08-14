#idade em dias ex010
#entrada
dias = int(input("Digite sua idade em dias: "))

#processamento
ano = dias//365
mes = dias//30 - ano*12
sobra = (dias%30)//2

print("""{} ano(s)
{} mes(es)
{} dias(s)""".format(ano, mes, sobra))