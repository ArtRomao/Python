def inverter(string):
    string = string.replace('0', '.')
    string = string.replace('1', '0')
    string = string.replace('.', '1')
    return string
    

input1 = (input("Insira um numero binario de 32 bits em complemento de dois:\n"))
input2 = (input("Insira outro numero binario de 32 bits em complemento de dois:\n"))

if len(input1) != 32 or len(input2) != 32:
    print("Quantidade de bits invalida em uma ou mais entradas.")
    exit(1)

if input1.isnumeric() == False or input2.isnumeric() == False:
    print("Caracter(es) invalido(s) inserido(s).")
    exit(1)
    
for i in range(len(input1)):
    if input1[i] != '0' and input1[i] != '1':
        print("Caracter(es) invalido(s) inserido(s).")
        exit(1)
        
for i in range(len(input2)):
    if input2[i] != '0' and input2[i] != '1':
        print("Caracter(es) invalido(s) inserido(s).")
        exit(1)
        
if input1[0] == '0':
    decimal1 = int(input1,2)

if input1[0] == '1':
    input1 = inverter(input1)
    decimal1 = -(int(input1,2) + 1)
    
if input2[0] == '0':
    decimal2 = int(input2,2)

if input2[0] == '1':
    input2 = inverter(input2)
    decimal2 = -(int(input2,2) + 1)
    
soma = decimal1 + decimal2

if soma >= 0:
    resultado = bin(soma)[2:].zfill(32)
    
    if resultado[0] == '1':
        resultado = '0' + resultado

elif soma < 0:
    resultado = bin(soma + 1)[3:].zfill(32)
    resultado = inverter(resultado)
    
print(str(decimal1) + ' + ' + str(decimal2) + ' = ' + str(soma))
print("\nResultado:\n" + resultado)