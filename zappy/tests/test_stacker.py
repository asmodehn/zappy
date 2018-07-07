import zappy
import pytest


def test_stacker_create_empty():
    s = zappy.Stacker()

    assert len(s) == 0


def test_stacker_create_iterable():
    s = zappy.Stacker((('a', 1), ('b', 2)))

    assert len(s) == 2
    assert s['a'] == 1
    with pytest.raises(KeyError):
        s['a']
    assert len(s) == 1
    assert s['b'] == 2
    with pytest.raises(KeyError):
        s['b']
    assert len(s) == 0


def test_stacker_create_kwargs():
    s = zappy.Stacker(a=1, b=2)

    assert len(s) == 2
    assert s['a'] == 1
    with pytest.raises(KeyError):
        s['a']
    assert len(s) == 1
    assert s['b'] == 2
    with pytest.raises(KeyError):
        s['b']
    assert len(s) == 0


def test_stacker_create_iterable_multi():
    s = zappy.Stacker((('a', 1), ('b', 2), ('a', 3)))

    assert len(s) == 2  # we only have two different keys
    assert s['a'] == 3  # confirming to stack semantics : Last In First Out
    assert len(s) == 2  # notice the length of dictionary doesnt change
    assert s['b'] == 2
    with pytest.raises(KeyError):
        s['b']
    assert len(s) == 1
    assert s['a'] == 1
    with pytest.raises(KeyError):
        s['a']
    assert len(s) == 0


# TODO : MultiDict behavior ?




if __name__ == '__main__':
    pytest.main([
        '-s', __file__,
])
