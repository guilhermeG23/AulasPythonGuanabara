velocidade = float(input('A velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce foi multado\nVocê dirigiu a mais de 80Km\h, sua multa é {:.2f}'.format(multa))
else:
    print('Velocidade abaixo do limite, sua velocidade {:.2f} Km\h'.format(velocidade))
