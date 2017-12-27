#Python 2.7
#Definindo Type valor
def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "Nope"
