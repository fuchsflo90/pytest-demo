"""Some fancy scripts."""
from datetime import date as _date
from sqlalchemy import create_engine as _create_engine

from utils import reverse_string as _reverse_string


def fizzbuzz(value: int) -> str:
    """Return some fizzbuzz string."""
    rules = {5: "fizz", 3: "buzz"}
    result = ""
    for key, term in rules.items():
        if value % key == 0:
            result += term
    return result


def store_to_database(table: str, records: list):
    """Store something in database."""
    query = f"insert into {table} values {str(records)}"

    sqlengine = _create_engine(
        "mysql://florian:fuchs@some.database/production"
    )

    # NOTE: usually we would use a with clause here!!
    connection = sqlengine.connect()
    connection.execute(query)


def get_reverse_date() -> str:
    """Get current timestamp."""
    return _reverse_string(str(_date.today()))
