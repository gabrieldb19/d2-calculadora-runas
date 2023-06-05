def rune(runa: int,a: int=1,num: int=1) -> int:
    """
    Esta wea genera un valor númerico para la runa usando como base 1=="El"
    Las runas van del 1 al 33.
    Las runas aumentan de valor de la siguiente forma:
        - De la 1 a 21 cada runa equivale a 3 de la anterior.
        - De la 22 a 33 cada runa equivale a 2 de la anterior.

    Args:
        runa (int): Número código de la runa entrante.
        a (int, optional): Variable para igualar a la runa entrante. Defaults to 1.
        num (int, optional): Valor númerico en "El" de la runa. Defaults to 1.

    Returns:
        Int: Valor númerico de la runa.

    Ejemplo:
        Si la runa entrante es "Tir"=3 - rune(3) => return 9
        "Tir" = 9 "El"
    """
    if runa<=33 or runa>=1:
        if runa>a:
            if a<21:
                num=rune(runa,a+1,num*3)
            elif a>=21:
                num=rune(runa,a+1,num*2)
        elif runa==a:
            num=num
        return num
    else:
        return None

def runes() -> dict:
    """
    Función que retorna un diccionario con clave/valor de las runas del diablo 2.

    Returns:
        dict: Devuelve un diccionario con...
            Key= Nombre de la runa.
            Value= Número código de la runa.
    """

    return {"El":1,"Eld":2,"Tir":3,"Nef":4,"Eth":5,"Ith":6,"Tal":7,"Ral":8,"Ort":9,"Thul":10,"Amn":11,"Sol":12,"Shael":13,"Dol":14,
        "Hel":15,"Io":16,"Lum":17,"Ko":18,"Fal":19,"Lem":20,"Pul":21,"Um":22,"Mal":23,"Ist":24,"Gul":25,"Vex":26,"Ohm":27,"Lo":28,
        "Sur":29,"Ber":30,"Jah":31,"Cham":32,"Zod":33}

def rune_result(run1: int,run2: int,cant: int=1) -> float:
    """ División de las runas entrantes.

    Args:
        run1 (int): Runa a dividir.
        run2 (int): Runa divisor.

    Returns:
        float: Devuelve la división de run1 entre run2.
    """

    run1=rune(run1)
    run2=rune(run2)

    return (run1*cant)/run2