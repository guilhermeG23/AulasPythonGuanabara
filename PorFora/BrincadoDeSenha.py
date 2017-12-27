#Brincando de senha
SECRET = 'senha'

#Ele compara a senha do input com a variavel, se erra ele printa erro, se acertar ele quebra o while
while True:
    password = input('Entre com sua senha: ')
    if password == SECRET:
        break
    print('Errou a senha!')

print('Bem vindo!')