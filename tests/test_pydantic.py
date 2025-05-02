from typing import Annotated

from pydantic import (
    UUID5,
    EmailStr,
    Field,
    NegativeFloat,
    NegativeInt,
    PositiveFloat,
    PositiveInt,
)
from pytest import mark, raises

from assertme.pydantic import WithPydantic


@mark.parametrize(
    "test_input,expected",
    [
        (10, WithPydantic(Annotated[int, Field()])),
        (10, WithPydantic(Annotated[int, Field(gt=9)])),
        (10, WithPydantic(PositiveInt)),
        (10.5, WithPydantic(PositiveFloat)),
        (-10, WithPydantic(NegativeInt)),
        (-10.5, WithPydantic(NegativeFloat)),
        ("01d2f0ce-8f47-56e4-9a9c-0f368406feb7", WithPydantic(UUID5, strict=True)),
        ("email@domain.com", WithPydantic(Annotated[str, EmailStr])),
        (
            {"email": "email@domain.com"},
            {"email": WithPydantic(Annotated[str, EmailStr])},
        ),
    ],
)
def test_with_pydantic(test_input, expected):
    assert test_input == expected


@mark.parametrize(
    "test_input,expected",
    [
        (10, WithPydantic(Annotated[str, Field()])),
        (8, WithPydantic(Annotated[int, Field(gt=9)])),
        (-10, WithPydantic(PositiveInt)),
        (-10.5, WithPydantic(PositiveInt)),
        (10, WithPydantic(NegativeInt)),
        (10.5, WithPydantic(NegativeFloat)),
        ("email-domain.com", WithPydantic(Annotated[str, EmailStr])),
        (
            {"email": "email-domain.com"},
            {"email": WithPydantic(Annotated[str, EmailStr])},
        ),
    ],
)
def test_with_pydantic_failues(test_input, expected):
    with raises(AssertionError):
        assert test_input == expected
