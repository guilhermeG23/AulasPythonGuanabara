#Biblioteca subprocesso sistema
import os
hostnameS = str(input('Entre com o Host: '))
print(os.system('ping {}'.format(hostnameS)))
