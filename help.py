import os

def clear():
    """ cls xD """
    os.system("cls")

def check(function):
    """ Decorador que verifica que el número ingresado este dentro de los párametros esperados.

    Args:
        funtion (int): Función que recibe por parametro un int que representa el límite de valores a verificar,
            devuelve el valor ingresado en el input en caso correcto, sino entra en bucle.
    """
    def wrapper(*args):
        while True:
            try:
                opcion = function(*args)
                if 0 < opcion <= args[0]:
                    return opcion
                else: 
                    clear() # Modificable segun contexto.
            except ValueError:
                    clear() # Modificable segun contexto.
    return wrapper

def checkRune(cod, dic) -> str:
    """ Esta wea devuelve el nombre de la runa segun su código. """
    for k,v in dic.items():
        if cod == v:
            return k