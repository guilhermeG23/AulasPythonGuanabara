#Python 2.7
#Codecademy

#Definindo Funcões no Python, Aprendendo como fazer

def spam():
  """Ovos"""
  print("Eggs!")

#Chamado com retorno
spam()

#Definicao com valor de entrada pela chamada
def square(n):
  squared = n ** 2
  print("{} Ao Quadrado {}".format(n, squared))
  return squared

#Insere valor de entrada e a equação imprimi o valor
square(10)

#Definindo melhor suas entradas

def power(base, exponent):
  result = base ** exponent
  print "%d to the power of %d is %d." % (base, exponent, result)

power(37, 4)

#Jogando a saida de uma def para outra

def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n)+ 2

#Outro modelo de entrada

def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")


