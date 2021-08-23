# Calculadora em Python 
############################

# Perguntar par o usuario qual a operação 
# Perguntar o primeiro numero 
# Perguntar o segundo numero 
# Calcular os dois valores 
# Imprimir o resultar na tela 

print('CALCULADORA INTELIGÊNTE')
print('Seja-vindo(a) \n')

nome = input('Qual seu nome?: \n')

while True: # loop de de enquanto ele for verdadeiro ele vai ficar rodando   

  operacao = input('Informe a operação (+,-,*,/) que você deseja realizar ou \'q\' para sair? ')
  if operacao == 'q' or operacao == "Q" :
    break

  elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/' :
  
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))

  if operacao == '+':
    total = num1 + num2
    print(total)
  elif operacao == '-':
    total = num1 - num2
    print(total)
  elif operacao == '*':
    total = num1 * num2
    print(total)
  elif operacao == '/':
    total = num1 / num2
    print(total)
  else:
    print('Operação inválida')


