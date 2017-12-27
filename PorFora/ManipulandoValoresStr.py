#Manupilando os Type STR
#Valor desformatado
valor = 'guiLhermE pastel de FRANGO'

#Valor original
print('Valor: {}'.format(valor))
#Minuscula
print('Valor: {}'.format(valor.lower()))
#maiuscula
print('Valor: {}'.format(valor.upper()))
#Capitalize, Deixa a primeira letra em maiusculo
print('Valor: {}'.format(valor.capitalize()))
#Deixa em maiusculo a primeira letra de cada palavra apos espaço
print('Valor: {}'.format(valor.title()))
#Substitui valor
print('Valor: {}'.format(valor.lower().replace('guilherme', 'teste')))
