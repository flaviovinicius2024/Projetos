idade = int(input('Qual a sua idade em dias?'))

A = idade / 365

M = (idade%365) / 30

D = (idade%365) % 30

print('{:.0f} ano(s) \n {:.0f} mes(es) \n {:.0f} dia(s)' .format(A, M, D))
