#Strings são imutaveis

# Possui 25 caraceters
frase = 'pastel de frango maligno'
# Imprimi tudo
print(frase)

#Fatiar

# imprimi so o valor do caracter 5 da variavel
print(frase[5])
# Imprimi do valor 5 a 15 dos caracteres da variavel
# O valor que ele vai realmente capturar vai ser de 5:14, o caracter 15 fica de fora
print(frase[5:15])
# Agora vamos testar a fatiação com o valor acima da maxima
print(frase[5:24])
# Transpondo a maxima
# Ele não da erro, simplismente imprimi o que estiver entre os valores
print(frase[5:30])
# Pulando casas, :2 ele ignora a casa entre dois
# Original = frase = 'pastel de frango maligno'
# EX: 'pse efag ain'
# A conta é assim: Valor final - 1 = casa a ser ignorada
print(frase[0:24:2])
print(frase[5:24:2])
# Fatiando, imprindo desde o inicio  e limitando a frase
print(frase[:5])
# Imprimindo a partir de um valor de caracteres
# Do caracter 20 até o final
print(frase[20:])
# Fatiando de modo inteligente com as tres casas
# A parteir do 5 até o fim pulando de duas em duas casas
print(frase[5::2])
# Tamanho das casas: Imprimi o numero de caracteres
print(len(frase))
# Contar quantas vezes um valor aparece dentro de uma string
# frase = <Variavel desejada>
# 'a' = <valor a ser procurado>
print(frase.count('a'))
# Contagem com fatiamento
# Conta os A's minusculos entre 0 a 12
print(frase.count('a', 0, 13))
# Procurar por posições especificas numa string
# Mostra o caracter que inicia o find
print(frase.find('fra'))
# O erro de nada encontrado no find
# Se ele mostrar -1 = não existe o valor
print(frase.find('teste123'))

# Operador
# Confirmar se um valor existe
# Ele tem como resultado True ou False
print('pastel' in frase)
print('frase' in frase)

# Métodos
# Transformacao
# Troca valor
# Replace valor1 por valor2
print(frase.replace('pastel', 'Errado'))
# Deixando maiusculo o valor da variavel
print(frase.upper())
# Deixando o valor da variavel em minusculo
print(frase.lower())
# Transforma tudo em minusculoe  deixa só o primeiro caractere em maiusculo
print(frase.capitalize())
# O title e um capitalize por palavra, ele indentifica onde a uma quebra de linha e transforma o primeiro valor antes da quebra de linhe numa letra em maiusculo
print(frase.title())

# Removendo todos os espaços inuteis antes e depois do valor de uma string
valor = ' Aprender Python '
# Sem strip
print(valor)
# Com strip
print(valor.strip())

# Não reconheceu o comando
# Removendo o valor de um unico lado(right) = diretia
# Direita
# print(valor.rstript())
# Esquerda
# print(valor.lstrip())

#split = ele encontra espaços numa variavel e tranforma num lista
#Ele pega uma string e divide em uma lista
print(frase.split())
#Juntando um valor
print(frase.split('-'.join(frase)))
#Ou
print('-'.join(frase))


#Imprimindo um texto
#Imprimi da forma que foi digitado, pulando as linha da mesma forma
print("""
#split = ele encontra espaços numa variavel e tranforma num lista
#Ele pega uma string e divide em uma lista
print(frase.split())
#Juntando um valor
print(frase.split('-'.join(frase)))
#Ou
print('-'.join(frase))
""")

#Utilizando mais de um comando por vez no objeto
print(frase.upper().count('a'))
print(frase.upper().count('A'))

#Alterando uma string
teste = ('pastel de frango maligno')
teste = frase.replace('pastel', 'bolo')
print(teste)