from enum import Enum


class Components(Enum):
    # Enumeración con el numero de segundos de cada componente
    # de la fecha
    year = 31536000
    day = 86400
    hour = 3600
    minute = 60
    second = 1


def format_duration(seconds: int):
    if seconds == 0:
        # Si seconds es igual a cero, la función devuelve "now"
        return "now"

    # Inicializamos dos variables, date una cadena vacía y
    # seconds_left cuyo valor inicial será seconds
    date = ""
    seconds_left = seconds

    for component in Components:
        # Iteramos sobre cada componente de la enumeración

        # Haremos una division entera de los segundos restantes entre el numero
        # de segundos del componente actual
        floor_division: int = seconds_left // component.value

        # Modificamos el valor de seconds_left para que sea el residuo de la division anterior
        seconds_left = seconds_left % component.value

        if floor_division >= 1:
            # Si el resultado de la division entera es mayor o igual a uno
            # el componente formará parte de la fecha
            date += f"{floor_division} {component.name}"
        if floor_division > 1:
            # Si el resultado de la division entera es estrictamente mayor a uno
            # se añadirá una "s" a la cadena
            date += "s"

        if floor_division >= 1 and seconds_left:
            # Si el resultado de la division entera es mayor o igual a 1 y
            # aun hay segundos restantes que contabilizar, se añadirá una
            # separación a la cadena
            date += ", "

    # Encontramos el indice de la ultima coma
    last_comma_index = date.rfind(",")

    # Reemplazamos la ultima coma por un "and" concatenando los caracteres iniciales
    # hasta el indice de la ultima coma, la cadena " and" y el resto de la cadena de la fecha
    date = date[:last_comma_index] + " and" + date[last_comma_index + 1 :]

    return date
