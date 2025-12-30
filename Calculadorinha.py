op = 0

print("Selecione a operacao:")
print("1 - Soma")
print("2 - Substracao")
print("3 - Multiplicacao")
print("4 - Divisao")
op = input("5 - Sair\n")
op = int(op)

if op==1:
    x = input("Primeira parcela: ")
    x = float(x)
    y = input("Segunda parcela: ")
    y = float(y)
    print('Soma:',x+y)

elif op==2:
    x = input("Minuendo: ")
    x = float(x)
    y = input("Subtraendo: ")
    y = float(y)
    print('Diferenca / Resto:',x-y)

elif op==3:
    x = input("Multiplicando: ")
    x = float(x)
    y = input("Multiplicador: ")
    y = float(y)
    print('Produto:',x*y)
    
elif op==4:
    x = input("Dividendo: ")
    x = float(x)
    y = input("Divisor: ")
    y = float(y)
    print('Quociente: ',x/y)
    print('Resto:',x%y)

elif op==5:
    print('Saindo...')
    
else:
    print('Opcao invalida.')