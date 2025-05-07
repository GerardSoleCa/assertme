from uuid import UUID

from pytest import mark, raises

from assertme.uuid import AnyStrUUID, AnyUUID


@mark.parametrize(
    "test_input,expected",
    [
        # UUID Object
        (UUID("07e56260-29b7-11f0-b48a-12756aaced90"), AnyUUID()),
        (UUID("0f9833c0-29b7-11f0-b48a-12756aaced90"), AnyUUID(version=1)),
        (UUID("b6602c76-f86e-32a2-ab42-71dd055ad3cc"), AnyUUID(version=3)),
        (UUID("5f455a36-48f2-44cb-bd79-ebb00b175208"), AnyUUID(version=4)),
        (UUID("01d2f0ce-8f47-56e4-9a9c-0f368406feb7"), AnyUUID(version=5)),
        (
            [
                UUID("01d2f0ce-8f47-56e4-9a9c-0f368406feb7"),
                UUID("01d2f0ce-8f47-56e4-9a9c-0f368406feb7"),
            ],
            [AnyUUID(version=5), AnyUUID(version=5)],
        ),
        # UUID String
        ("07e56260-29b7-11f0-b48a-12756aaced90", AnyStrUUID()),
        ("0f9833c0-29b7-11f0-b48a-12756aaced90", AnyStrUUID(version=1)),
        ("b6602c76-f86e-32a2-ab42-71dd055ad3cc", AnyStrUUID(version=3)),
        ("5f455a36-48f2-44cb-bd79-ebb00b175208", AnyStrUUID(version=4)),
        ("01d2f0ce-8f47-56e4-9a9c-0f368406feb7", AnyStrUUID(version=5)),
    ],
)
def test_any_uuid(test_input, expected):
    assert test_input == expected


@mark.parametrize(
    "test_input,expected",
    [
        (10, AnyStrUUID()),
        # UUID Object
        ("07e56260-29b7-11f0-b48a-12756aaced90", AnyUUID()),
        (UUID("0f9833c0-29b7-11f0-b48a-12756aaced90"), AnyStrUUID(version=5)),
        (UUID("b6602c76-f86e-32a2-ab42-71dd055ad3cc"), AnyStrUUID(version=4)),
        (UUID("5f455a36-48f2-44cb-bd79-ebb00b175208"), AnyStrUUID(version=3)),
        (UUID("01d2f0ce-8f47-56e4-9a9c-0f368406feb7"), AnyStrUUID(version=1)),
        # UUID String
        (UUID("07e56260-29b7-11f0-b48a-12756aaced90"), AnyStrUUID(version=1)),
        ("0f9833c0-29b7-11f0-b48a-12756aaced90", AnyStrUUID(version=5)),
        ("b6602c76-f86e-32a2-ab42-71dd055ad3cc", AnyStrUUID(version=4)),
        ("5f455a36-48f2-44cb-bd79-ebb00b175208", AnyStrUUID(version=3)),
        ("01d2f0ce-8f47-56e4-9a9c-0f368406feb7", AnyStrUUID(version=1)),
    ],
)
def test_any_uuid_failues(test_input, expected):
    with raises(AssertionError):
        assert test_input == expected
