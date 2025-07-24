while True:
  first_num = int(input('Primeiro valor: '))
  second_num = int(input('Segundo valor: '))
  operations = int(input('''
  1-Somar
  2-Subtrair
  3-Mutiplicar
  4-Dividir
  5-Sair
  '''))
  result = 0
  if operations == 1:
    result = first_num + second_num
  elif operations == 2:
    result = first_num - second_num
  elif operations == 3:
    result = first_num * second_num
  elif operations == 4:
    result = first_num / second_num
  else:
    print('...finalizando')
    print('Programa encerrado!')
    break
  print(f'Resultado= {result}')