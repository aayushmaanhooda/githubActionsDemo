from src.opertation import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0
    assert add(10,10) == 20


def test_sub():
    assert sub(5,3) == 2
    assert sub(1,1) == 0
    assert sub(10,1) == 9