def valor(g1):
    return g1 * g1

def valor1(g2):
    return g2 * g2

def teste(g1, g2):
    return valor(g1) + valor1(g2)

t1 = float(input('Valor 1: '))
t2 = float(input('Valor 2: '))

print('Valor final: {}'.format(teste(t1, t2)))
