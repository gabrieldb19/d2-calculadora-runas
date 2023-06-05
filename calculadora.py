from cheats import runes, rune_result
from help import *

@check
def customInput(limite: int, texto: str) -> int:
    """ Muestra un texto por consola y recibe un input. Devuelve el input.

    Args:
        limite (int): Limite de números enteros validos entre 1 y "limite" inclusive.
        texto (str): Texto a mostrar previo a la petición de input.

    Returns:
        int: Número ingresado.
    """
    print(texto)
    opcion = int(input ("> "))
    return opcion

runas = runes()

# Calculadora de runas por consola - En bucle
while True:
    clear()
    opcion = customInput(3,"""***********************
D2 Calculadora de Runas
***********************
1 - Calcular
2 - Mostrar lista
3 - Salir
    """)
    clear()

    if opcion == 2:
        for k,v in runas.items():
            print (f"{k} - {v}")

    if opcion == 1 or opcion == 2:
        runa1 = customInput(33, "Introduce el código de la runa:")
        runa2 = customInput(33, "Introduce el segundo código:")

        print (f"La runa {checkRune(runa1, runas)} es igual a {rune_result(runa1, runa2)} {checkRune(runa2, runas)}")

        import time
        time.sleep(3)

    if opcion == 3:
        break