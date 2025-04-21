
###################################### FUNCION #############################################

def binario_decimal():

    while True:
        digito=0 #Variable que va a guardar el digito (0,1) para ser multiplicado por 2^exponente
        exponente=-1 #No lo inicializo en 0 porque sino la potencia va a comenzar en 2^1 y necesito como primer potencia 2^0
        decimal=0 #Variable que va guardando el peso de cada digito (0,1)*2^exponente
        total=0 #Variable que suma el peso de cada digito para obtener el total y asi dar con el equivalente decimal del numero binario ingresado

        try:
            print("Ingrese el numero binario que desea convertir en decimal o escriba 'exit' para salir:")
            entrada=input()
            
            if entrada.lower() == "exit": 
                return "exit"
            
            num_binario=int(entrada) #Variable que contiene el numero binario a convertir

            while num_binario>0: #El bucle se termina despues de que num_binario sea de una cifra
                exponente=exponente + 1 #Contador para el exponente de la potencia 
                digito=num_binario % 10 #Obtengo el digito de menor peso binario
                if digito == 1 or digito == 0: #Para chequear que sea un numero binario y no cualquier otro formato
                    decimal=(2 ** exponente) * digito #Obtengo el peso del digito binario
                    num_binario=num_binario // 10 #Elimina digito a digito, de menor a mayor peso binario.
                    total=total+decimal #Sumo los pesos binario obtenidos para obtener el resultado final (decimal)
                else: #Para salir del bucle si hay algun numero distinto de 1 o 0 
                    num_binario = str(num_binario) #Al convertit num_binario en un str se salta todo el while y pasa directamente al except por ser un error
            return total
        except:
            print("El numero ingresado no corresponde a un numero binario") #Repite la instruccion hasta que se ingrese un numero entero

###################################################################################################################

prueba = binario_decimal()
if prueba == "exit":
    print("Usted a salido del programa. Hasta luego!")
else:
    print("El numero binario ingresado en decimal es",prueba)