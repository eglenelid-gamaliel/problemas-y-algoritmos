def valid_parentheses(parens: str):
    parens_list: list[str] = []

    if parens.startswith(")") or parens.endswith("("):
        return False

    for paren in parens:
        parens_list.append(paren)

        if paren == ")":
            closing_index = parens_list.index(")")
            previous_index = closing_index - 1

            if parens_list[previous_index] == "(":
                parens_list.pop(closing_index)
                parens_list.pop(previous_index)
            else:
                return False

    if not parens_list:
        return True
