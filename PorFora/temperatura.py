temperatura = float(input('Temperatura atual: '))

if temperatura <= 16.9:
    print('Ta frio')
elif temperatura >= 17 and temperatura <= 20.9:
    print('Menos frio')
elif temperatura >= 21 and temperatura <= 24.9:
    print('Morno')
elif temperatura >= 25 and temperatura <= 32:
    print('Quente')
else:
    print('Muito calor')

