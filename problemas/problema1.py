def valid_parentheses(parens: str):
    # Lista auxiliar con los paréntesis que no han sido cerrados
    parens_list: list[str] = []

    # Si la cadena de paréntesis inicia o termina de una manera incorrecta no es necesario
    # realizar el resto de comprobaciones
    if parens.startswith(")") or parens.endswith("("):
        return False

    for paren in parens:
        # Se itera sobre los caracteres de la cadena
        # Cada paréntesis se añade a la lista auxiliar
        parens_list.append(paren)

        if paren == ")":
            # Si el caracter actual es un paréntesis de cierre se verifica que el
            # caracter anterior sea un paréntesis de apertura
            closing_index = parens_list.index(")")
            previous_index = closing_index - 1

            if parens_list[previous_index] == "(":
                # Si la condición se cumple, se retiran ambos elementos de la
                # lista auxiliar
                parens_list.pop(closing_index)
                parens_list.pop(previous_index)
            else:
                return False

    if not parens_list:
        # Si al finalizar la iteración no hay paréntesis por cerrar
        # la cadena es valida
        return True
