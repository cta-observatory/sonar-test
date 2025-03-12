import pytest


FIBS = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

@pytest.mark.parametrize(("n", "expected"), enumerate(FIBS))
def test_fib(n, expected):
    from test_sonar import fib
    assert fib(n) == expected

def test_negative():
    """Test we get a good error message for negative input."""
    from test_sonar import fib

    with pytest.raises(ValueError, match="n must be >=0, got -1"):
        fib(-1)

    with pytest.raises(ValueError, match="n must be >=0, got -100"):
        fib(-100)
