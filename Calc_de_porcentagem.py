#Calculadora de porcentagem

V = int(input('Qual o valor base? '))

P = int(input('Qual a porcentagem? '))

R = V * (P/100)

print('{}% de {} é igual a {}' .format(P, V, R))
