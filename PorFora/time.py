#!/python/python
# hora2.py - CGI que exibe continuamente hora local do servidor
from time import time, localtime
h, m, s = localtime(time())[3:6]
print('Hora: %02d:%02d:%02d' % (h, m, s))


