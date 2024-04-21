print ('Olá, seja bem-vindo(a) ao programa de mini calculadora. Vamos lá.')

while True:
    n1= input('Digite um número inicial: ')
    n2 = input('Digite o segundo número: ')
    operador = input ('Digite o operador (+ - / * ): ')

    num_validos = None
    n1_float = 0
    n2_float = 0

    try:
        n1_float = float(n1)
        n2_float = float(n2)
        num_validos = True

    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_on = '+-/*'

    if operador not in operadores_on:
        print('Operador inválido.') # caso digite um operador não descrito pelo programa
        continue
    if len(operador) > 1: # quantidade de operadores é APENAS UMA
        print('Digite apenas um operador.') # caso for mais de 1, ele printa o que está abaixo
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+': 
        print(n1_float + n2_float)  # operação de soma
    elif operador == '-':
        print(n1_float - n2_float)  # operação de subtração 
    elif operador == '/':
        print(n1_float / n2_float)  # operação de divisão
    elif operador == '*':
        print(n1_float * n2_float) # operação de multiplicação
    else:
        print('nao deveria chegar aqui.')

    sair = input ('Quer sair ? [s]im: ') #opção de saida do programa 
    sair = sair.lower().startswith('s') #converete maiúsculo para minusculo/se começa com tal letra
    
    if sair is True:
        break