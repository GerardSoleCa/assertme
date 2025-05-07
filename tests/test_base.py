from typing import Callable

from pytest import raises

from assertme.base import Anything


class NoOpAnything(Anything):
    def _check_methods(self) -> list[Callable]:
        return super()._check_methods()  # type: ignore


class MockAnything(Anything):
    def _check_methods(self) -> list[Callable]:
        return []


def test_eq():
    assert 1 == MockAnything()


def test_ne():
    with raises(AssertionError):
        assert 1 != MockAnything()


def test_none_check():
    assert {"field": None} != {"field": MockAnything()}
    with raises(AssertionError):
        assert {"field": None} == {"field": MockAnything()}


def test_repr():
    mock_anything = MockAnything()
    assert {"field": None} != {"field": mock_anything}
    assert mock_anything.__repr__() == "<MockAnything(Object is None)>"


def test_check_methods_not_implemented():
    with raises(NotImplementedError):
        assert 1 == NoOpAnything()
