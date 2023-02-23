from problemas.problema3 import movie


def test_movie():
    assert movie(500, 15, 0.9) == 43
    assert movie(100, 10, 0.95) == 24
