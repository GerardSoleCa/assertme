from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from pytest import mark, raises

from assertme.datetime import AnyDatetime, AnyStrDatetime, DateType


UTC = timezone.utc
TZ_MADRID = ZoneInfo("Europe/Madrid")


@mark.parametrize(
    "test_input,expected",
    [
        (datetime(2024, 12, 1), AnyDatetime()),
        (datetime(2024, 12, 1), AnyDatetime(datetype=DateType.PAST)),
        (datetime(2222, 12, 1), AnyDatetime(datetype=DateType.FUTURE)),
        (datetime(2024, 12, 1), AnyDatetime(tz=None)),
        (datetime(2024, 12, 1, tzinfo=UTC), AnyDatetime(tz=UTC)),
        (
            datetime(2024, 12, 1, tzinfo=TZ_MADRID),
            AnyDatetime(tz=TZ_MADRID),
        ),
    ],
)
def test_any_datetime(test_input, expected):
    assert test_input == expected


@mark.parametrize(
    "test_input,expected",
    [
        (None, AnyDatetime()),
        (1, AnyDatetime()),
        ("1", AnyDatetime()),
        (datetime(2024, 12, 1), AnyDatetime(datetype=DateType.FUTURE)),
        (datetime(2222, 12, 1), AnyDatetime(datetype=DateType.PAST)),
        (datetime(2024, 12, 1), AnyDatetime(tz=TZ_MADRID)),
        (datetime(2024, 12, 1, tzinfo=UTC), AnyDatetime(tz=TZ_MADRID)),
        (datetime(2024, 12, 1, tzinfo=TZ_MADRID), AnyDatetime(tz=UTC)),
    ],
)
def test_any_datetime_failures(test_input, expected):
    with raises(AssertionError):
        assert test_input == expected


@mark.parametrize(
    "test_input,expected",
    [
        # Only date
        ("1991-12-31", AnyStrDatetime()),
        ("1991-12-31", AnyStrDatetime(datetype=DateType.PAST)),
        ("2222-12-31", AnyStrDatetime(datetype=DateType.FUTURE)),
        # Date and Time
        ("1991-12-31T13:09:30.526526", AnyStrDatetime()),
        ("1991-12-31T13:09:30.526526", AnyStrDatetime(datetype=DateType.PAST)),
        ("2222-12-31T13:09:30.526526", AnyStrDatetime(datetype=DateType.FUTURE)),
        ("1991-12-31T13:09:30.526526Z", AnyStrDatetime(tz=UTC)),
        ("2025-05-02 15:25:25.526526+02:00", AnyStrDatetime(tz=TZ_MADRID)),
    ],
)
def test_any_str_datetime(test_input, expected):
    assert test_input == expected


@mark.parametrize(
    "test_input,expected",
    [
        (datetime(2024, 12, 1), AnyStrDatetime()),
        # Only date
        ("31/12/1991", AnyStrDatetime()),
        ("31/12/1991", AnyStrDatetime(datetype=DateType.PAST)),
        ("31/12/2222", AnyStrDatetime(datetype=DateType.FUTURE)),
        ("12/31/1991", AnyStrDatetime()),
        ("12/31/1991", AnyStrDatetime(datetype=DateType.PAST)),
        ("12/31/2222", AnyStrDatetime(datetype=DateType.FUTURE)),
        ("2222/12/31", AnyStrDatetime(datetype=DateType.FUTURE)),
        # Date and Time
        ("1991-12-31T13:09:30.526", AnyStrDatetime(tz=UTC)),
        ("1991-12-31T13:09:30.526", AnyStrDatetime(datetype=DateType.FUTURE)),
        ("2222-12-31T13:09:30.526", AnyStrDatetime(datetype=DateType.PAST)),
        ("1991-12-31T13:09:30.526Z", AnyStrDatetime()),
        ("2025-05-02 15:25:25.895467+02:00", AnyStrDatetime(tz=UTC)),
    ],
)
def test_any_str_datetime_failures(test_input, expected):
    with raises(AssertionError):
        assert test_input == expected
