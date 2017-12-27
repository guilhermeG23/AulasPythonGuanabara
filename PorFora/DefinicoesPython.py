#Defifnicao, recebe uma variavel e recebe uma entrada ou qualquer coisa do tipo para gerar um retorno a funcao principal
def increment(x):
    return x + 1

print(increment(3))

entrada = int(input('Digite a entrada INT: '))
x = entrada
print(increment(x))
