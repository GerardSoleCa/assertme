from pytest import mark, raises

from assertme.instance import InstanceOf


@mark.parametrize(
    "test_input,expected",
    [
        (1, InstanceOf(int)),
        ("a", InstanceOf(str)),
        ({"field", 1}, InstanceOf(set)),
        ({"field": 1}, {"field": InstanceOf(int)}),
        ({"field": 1.9}, {"field": InstanceOf(float)}),
        ({"field": {}}, {"field": InstanceOf(dict)}),
    ],
)
def test_instance_type(test_input, expected):
    assert test_input == expected


@mark.parametrize(
    "test_input,expected",
    [
        (1, InstanceOf(str)),
        ("a", InstanceOf(int)),
        ({"field", 1}, InstanceOf(list)),
        ({"field": 1}, {"field": InstanceOf(str)}),
        ({"field": 1.9}, {"field": InstanceOf(int)}),
        ({"field": {}}, {"field": InstanceOf(list)}),
    ],
)
def test_instance_type_failure(test_input, expected):
    with raises(AssertionError):
        assert test_input == expected
