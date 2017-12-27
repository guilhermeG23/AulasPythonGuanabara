#Bibliotecas
import platform
import socket
#Captura o valor do sistema operacional
so = platform.system()
#IP da Machine
ip = socket.gethostbyname(socket.gethostname())
#Imprimi o modelo da plataforma
print('Seu sistema operacional: {}'.format(so))
ValorSO = "Arquitetura do CPU: {}\nMachine Name Network: {}\nInfo S.O: {}\nIP: {}".format(platform.machine(), platform.node(), platform.platform(), ip)
#Imprimi qual plataforma ele pertence, de forma mais elegante
if so == 'Windows':
    print('Seu sistema Operacional e o Microsoft Windows')
    print(ValorSO)
elif so == 'Darwin':
    print('Seu sistema e o Apple Mac OS')
    print(ValorSO)
elif so == 'Linux':
    print('Seu sistema e uma Distro Linux')
    print(ValorSO)
else:
    print('Sistema nao encontrado')
    print(ValorSO)
