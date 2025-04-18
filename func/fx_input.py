def input_fx():
    while True:
        try:
            var = input('Ingrese un número entero u oprima e para salir')
            if(var.lower() == 'e'): return 'e'
            var = int(var)
            return var
        except:
            print('Por favor ingrese un número entero')

var = input_fx()
if(var == 'e'): 
    print('Ha salido del programa')
else:
    print(var)
