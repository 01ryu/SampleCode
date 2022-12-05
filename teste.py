print('O programa tem o intuito de aprovar um empréstimo bancário para a compra de uma casa')
x = float(input('Para isso, forneça o valor da casa: '))
y = float(input('Forneça o valor do seu salário: '))
z = float(input('Forneça também, em quantos anos, a dívida será quitada: '))
a = x * 12
b = x / z
c = x * 0.30
if b > c:
   print('O valor do empréstimo foi negado')
else:
  print('O valor do empréstimo foi aprovado.')
