import zappy
import pytest


@zappy.pure
def print_fun():
    print(42)


def test_print_fun_raises():
    with pytest.raises(zappy.ZAPImpurityDetected):
        print_fun()


if __name__ == '__main__':
    import pytest
    pytest.main([
        '-s', __file__,
])
