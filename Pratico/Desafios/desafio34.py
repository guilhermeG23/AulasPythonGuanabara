#Meu jeito

salario = float(input('Seu salario: '))
if salario >= 1250:
    print('Seu salario é {:.2f}\nSeu aumento é {:.2f}\nSeu salario final é {:.2f}'.format(salario, (salario / 10), salario + (salario / 10)))
else:
    print('Seu salario é menor que 1250\nSeu salario é {:.2f}\nSeu aumento é {:.2f}\nSalario final é {:.2f}'.format(salario, ((salario / 100) * 15), salario + ((salario / 100) * 15)))

#Guanabara

salario = float(input('Seu salario: '))
if salario >= 1250:
    aumento = (salario / 10)
    salarioNovo = aumento + salario
else:
    aumento =  (salario / 100) * 15
    salarioNovo = aumento + salario
print('Seu antigo salario {:.2f}\nSeu aumento {:.2f}\nSalario atual: {:.2f}'.format(salario, aumento, salarioNovo))
