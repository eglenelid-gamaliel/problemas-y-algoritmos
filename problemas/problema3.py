def movie(card: float, ticket: float, perc: float):
    loop: int = 0

    system_b_price = card
    ticket_b = ticket * perc

    while True:
        loop += 1

        system_a_price = ticket * loop
        system_b_price = system_b_price + ticket_b

        if round(system_b_price) < system_a_price:
            break
        else:
            ticket_b = ticket_b * perc

    return loop
