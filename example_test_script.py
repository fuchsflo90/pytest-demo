"""Tests for my script."""
import pytest as _pytest
from script import (
    fizzbuzz as _fizzbuzz,
    get_reverse_date as _get_reverse_date,
    store_to_database as _store_to_database,
)


def test_fizzbuzz():
    """Test fizzbuzz function."""
    assert _fizzbuzz(5) == "fizz"
    assert _fizzbuzz(12) == "buzz"
    assert _fizzbuzz(15) == "fizzbuzz"


@_pytest.mark.freeze_time("1900-05-04")
def test_get_reverse_date():
    """Test get reverse date function."""
    assert _get_reverse_date() == "40-50-0091"


def test_store_to_database(mocker):
    """Test store to database function."""
    mock_connection = mocker.MagicMock()
    mock_engine = mocker.MagicMock()

    mock_engine.connect.return_value = mock_connection
    mock_create_engine = mocker.patch(
        "script._create_engine", return_value=mock_engine
    )

    records = ("stefan", "mo", "nikita", "ravi", "flo")
    table = "data_intelligence"
    expected_query = (
        "insert into data_intelligence values "
        "('stefan', 'mo', 'nikita', 'ravi', 'flo')"
    )

    _store_to_database(table=table, records=records)

    mock_create_engine.assert_called_once_with(
        "mysql://florian:fuchs@some.database/production"
    )

    mock_engine.connect.assert_called_once()
    mock_connection.execute.assert_called_once_with(expected_query)
