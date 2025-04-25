from func.fx_input import parse_input, exit_test
from func.decimal_binario import dec_bin
from func.binario_decimal import bin_dec
from func.hexa import hexa

def main_loop():
    while True:
        print('¡Bienvenido/a al conversor de números!')
        print('Por favor seleccione que operación desea realizar:')
        print('1. Binario a decimal \n2. Decimal a binario \n3. Hexadecimal <-> Decimal')
        print('Para salir ingrese E')
        opt = parse_input(int, '', 'Por favor ingrese una opción válida', lambda var: var in [1,2,3] )
        if(exit_test(opt)): return
        match opt:
            case 1: bin_dec()
            case 2: dec_bin()
            case 3: hexa()

main_loop()