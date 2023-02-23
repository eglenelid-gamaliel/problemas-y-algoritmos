from problemas.problema1 import valid_parentheses


def test_valid_parentheses():
    assert valid_parentheses("()") == True
    assert valid_parentheses(")(()))") == False
    assert valid_parentheses("(") == False
    assert valid_parentheses("(())((()())())") == True
