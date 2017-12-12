nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
#A estrutura resumida tambem funciona normalmente
if media >= 5:
    print('Você tirou mais de 5')
    print('Sua média é: {:.2f}'.format(media))
else:
    print('Sua média é menor que 5\nSua média é {:.2f}'.format(media))
print('--FIM--')
