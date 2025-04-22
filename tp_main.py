from func.fx_input import parse_input, exit_test

def main_loop():
    print('¡Bienvenido/a al conversor de números!')
    print('Por favor seleccione que operación desea realizar:')
    print('1. Binario a decimal \n2. Decimal a binario \n3. Hexa u Octal')
    print('Para salir ingrese E')
    opt = parse_input(int, '', 'Por favor ingrese una opción válida', lambda var: var in [1,2,3] )
    if(exit_test(opt)): return
    match opt:
        case 1: print('Binario a decimal')
        case 2: print('Decimal a binario')
        case 3: print('Decimal a Hexadecimal')

main_loop()