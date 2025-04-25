def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    
    binario = ""
    numero = decimal
    
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    
    return binario

# Pedir número al usuario
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir y mostrar resultado
resultado = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es: {resultado}")
