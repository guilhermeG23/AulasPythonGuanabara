#Limitando a entrada de strings
x = 'Hello word Pastel de frango'
print(x[0:5])
print('Quebrado em duas impressoes por limitadores de caracteres de impressao')
print(x[6:10])

#Pulando casas na impressao
print(x[::2])
print(x[1::2])

#Invertendo a impressao
print(x[::-1])

#Dividindo sequencias de strings baseada do espaço entre caracteres
print(x.split())

#Limitando os split, ele so vai fazer uma split
print(x.split(maxsplit=1))

x = x.split()

#Unindo valores de uma lista
print(' '.join(x))
