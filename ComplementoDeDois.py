try:
    decimal = int(input("Insira um numero decimal: "))
    bits = int(input("Insira a quantidade de bits: "))
except:
    print("Insira apenas numeros inteiros. ")
    exit(1)

if decimal >= 0:
    binario = bin(decimal)[2:].zfill(bits)
    
    if len(binario) >= bits or bits <= 1:
        binario = '0' + binario
        bits = len(binario);
        print("Quantidade de bits excedida, o tamanho foi atualizado para " + str(bits) + '.')
elif decimal < 0:
    binario = bin(decimal + 1)[3:].zfill(bits)
    binario = binario.replace('0', '.')
    binario = binario.replace('1', '0')
    binario = binario.replace('.', '1')
    
    if len(binario) >= bits or bits <= 1:
        binario = '1' + binario
        bits = len(binario);
        print("Quantidade de bits excedida, o tamanho foi atualizado para " + str(bits) + '.')
    
octal = oct(int(binario, 2))[2:]
hexadecimal = hex(int(binario, 2))[2:]

print("Complemento de dois de " + str(decimal) + " em:")
print(" - Binario: " + binario)
print(" - Octal: " + octal)
print(" - Decimal: " + str(int(binario, 2)))
print(" - Hexadecimal: " + hexadecimal)