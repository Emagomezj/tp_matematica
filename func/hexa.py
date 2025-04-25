def hexa():
    # Menu de opciones

    opcion = input("Qué conversión desea hacer?\n1 - Convertir Decimal a Hexadecimal\n2 - Convertir Hexadecimal a Decimal\nElije una opción: ")

    # Decimal a Hexa
    if opcion == "1":
        decimal = int(input("Ingrese un número decimal: "))
        hexaTexto = ""   # Contiene resultado final como cadena
        cociente = decimal  # Usamos para dividir entre 16 sucesivamente

        # Bucle para dividir entre 16
        while cociente > 0:
            resto = cociente % 16    # Otenemos el resto que será un dígito hexadecimal
            cociente = cociente // 16  # División entera

            # Convertimos el resto en carácter hexadecimal
            if resto < 10:
                caracter = str(resto)  # si el número está entre 0 y 9, convertimos a texto.
            
                # Transformamos la letra coorrespondiente a hexadecimal
            elif resto == 10:
                caracter = "A"
            elif resto == 11:
                caracter = "B"
            elif resto == 12:
                caracter = "C"
            elif resto == 13:
                caracter = "D"
            elif resto == 14:
                caracter = "E"
            elif resto == 15:
                caracter = "F"

            # Agregamos los caracteres al principio de hexaTexto
            hexaTexto = caracter + hexaTexto

        # Si el decimal es = 0, devolvemos "0"
        if hexaTexto == "":
            hexaTexto = "0"

        print("El número hexadecimal es:", hexaTexto)

    # Hexa a Decimal
    elif opcion == "2":

        # Leemo el númeor hexa como texto
        hexaTexto = input("Ingrese un número hexadecimal (en mayúsculas): ")
        # Número decimal acumulado
        resultadoDecimal = 0
        # Potencia de 16
        valor = 1

        # Recorremos el número hexadecimal de derecha a izquierda
        for i in range(len(hexaTexto) - 1, -1, -1): # range para recorrer los caracteres del final a inicio
            digito = hexaTexto[i]  # Tomamos uno por uno los caracteres

            # Devolvemos el valor correspondiente de 10 a 15
            if digito == "A":
                decimal = 10
            elif digito == "B":
                decimal = 11
            elif digito == "C":
                decimal = 12
            elif digito == "D":
                decimal = 13
            elif digito == "E":
                decimal = 14
            elif digito == "F":
                decimal = 15
            else:
                decimal = int(digito)

            # Sumamos al resultado usando potencia de 16
            # Multiplicamos el valor del dígito por su posición y sumamos ese resultado al total
            resultadoDecimal += decimal * valor
            valor *= 16

        print("El número decimal es: ", resultadoDecimal)

    # opcion inválida
    else:
        print("Opción inválida.")

