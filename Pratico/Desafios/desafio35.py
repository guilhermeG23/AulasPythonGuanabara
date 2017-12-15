#Meu jeito

lado1 = float(input('lado 1: '))
lado2 = float(input('lado 2: '))
lado3 = float(input('lado 3: '))

#A medida de qualquer um dos lados é menor que a soma das medidas dos outros dois lados e maior que o valor absoluto entre a diferença da medida dos outros dois lados.

if lado1 < (lado2 + lado3) and lado1 > (lado2 - lado3):
    if lado2 < (lado1 + lado3) and lado2 > (lado1 - lado3):
        if lado3 < (lado2 + lado1) and lado3 > (lado1 - lado2):
            print('Forma triangulo')
        else:
            print('Não forma')
    else:
        print('Não forma')
else:
    print('Não forma')

#Jeito guanabara

lado1 = float(input('lado 1: '))
lado2 = float(input('lado 2: '))
lado3 = float(input('lado 3: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('Forma triangulo')
else:
    print('Não forma triangulo')
