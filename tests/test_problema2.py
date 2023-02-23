from problemas.problema2 import format_duration


def test_format_duration():
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
