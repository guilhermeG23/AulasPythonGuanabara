print('Voce vai viajar!')
valor = float(input('Quantos Km você vai rodar: '))

if valor < 200:
    print('Você vai pagar de passagem {:.2f} por {:.2f} Km'.format(valor * 0.5, valor))
else:
    print('A viagem tem mais de 200Km, você vai pagar {:.2f} por {:.2f} Km'.format(valor * 0.45, valor))

#Operador resumido guanabara
#O preco vai receber ou "isto ou aquilo"
preco = valor * 0.5 if valor <= 200 else valor * 0.45
print('A viagem tem mais de 200Km, você vai pagar {:.2f} por {:.2f} Km'.format(preco, valor))
