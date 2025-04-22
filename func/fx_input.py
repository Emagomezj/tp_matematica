# Función para testear si se da el comando de salir
def exit_test(var):
    return str(var).lower() == 'e'

# Handler de inputs
def parse_input(pars, frase, err, condition = lambda x: True):
    while True:
        try:
            var = input(frase)
            if(exit_test(var)):
                return var
            pars_var = pars(var)
            if(condition(pars_var)):
                return pars_var
            else:
                raise ValueError(err)
        except:
            print(err)

        
            