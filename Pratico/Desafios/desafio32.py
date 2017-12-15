#Ano bissexto

#from datetime import datetime
#now = datetime.now()
#print now.year
#print now.month
#print now.day
#print now.hour
#print now.minute
#print now.second

#Modulo de anos
from datetime import datetime

ano = int(input('Digite o ano para ver se é bissexto, digite 0 para usar o ano atual: '))

#Receber ano atual , Meu jeito
if ano == 0:
    ano = datetime.now()
    ano = ano.year

#Guanabara
#if ano == 0:
#   ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano é Bissexto! Ano {}'.format(ano))
else:
    print('Ano não é Bissexto! {}'.format(ano))





