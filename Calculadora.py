n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2

result = int(input('1. Soma \n'  
                   '2. Subtração \n'
                   '3. Multiplicação \n'
                   '4. Divisão \n \n'
                   'R:'))



if result == 1:
     print('{} + {} = {}' .format(n1, n2, soma))

elif result == 2:
     print('{} - {} = {}' .format(n1, n2, sub))

elif result == 3:
    print('{} * {} = {}' .format(n1, n2, mul))

elif result == 4:
     print('{} / {} = {}' .format(n1, n2, div))
