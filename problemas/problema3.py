def movie(card: float, ticket: float, perc: float):
    # Inicializamos una variable auxiliar "loop" para contar las visitas al cine
    loop: int = 0

    # Inicializamos el precio del sistema b con el costo de la tarjeta y calculamos
    # el costo del primer boleto del sistema b
    system_b_price = card
    ticket_b = ticket * perc

    # Usaremos un ciclo while para realizar los cálculos
    while True:
        # Se suma 1 al numero de visitas
        loop += 1

        # Se calcula el precio del sistema a
        system_a_price = ticket * loop

        # Se suma el precio del boleto b al precio del sistema b
        system_b_price = system_b_price + ticket_b

        if round(system_b_price) < system_a_price:
            # Si el precio redondeado del sistema b es menor al del sistema a
            # detenemos el ciclo while
            break
        else:
            # De lo contrario calculamos el precio del siguiente boleto del
            # sistema b
            ticket_b = ticket_b * perc

    # Al finalizar el ciclo while la función devuelve "loop" es decir el numero de visitas
    return loop
