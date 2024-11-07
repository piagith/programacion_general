


def asignar_mensaje(promedio: float) -> str:

    '''
    parametro: promedio (float)
    
    retorno: mensaje (str)
    '''

    if (promedio < 2):
        mensaje = "tenes que caminar mas"
    elif (promedio >= 2) and (promedio <=5):
        mensaje = "buen trabajo"
    else:
        mensjae = "excelente rendimiento"
    return  mensaje

TOTAL_DIAS = 2
cantidad_perros_mas_4 = 0
flag_primer_perro = True
lista_perros = []

