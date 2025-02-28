import pytest
import datetime
from unittest.mock import patch
from app.main import outdated_products


@pytest.mark.parametrize(
    "today_date, products, expected",
    [
        (
            datetime.date(2022, 2, 2),
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
                {"name": "duck", "expiration_date":
                    datetime.date(2022, 2, 1), "price": 160},
            ],
            ["duck"],
        ),
        (
            datetime.date(2022, 3, 1),
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
                {"name": "duck", "expiration_date":
                    datetime.date(2022, 2, 1), "price": 160},
            ],
            ["salmon", "chicken", "duck"],
        ),
        (
            datetime.date(2022, 1, 1),
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
            ],
            [],
        ),
        (
            datetime.date(2022, 2, 5),
            [
                {"name": "milk", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 50},
                {"name": "bread", "expiration_date":
                    datetime.date(2022, 2, 4), "price": 30},
            ],
            ["bread"],  # "bread" просрочен, но "milk" - нет
        ),
    ],
)
def test_outdated_products(today_date: datetime,
                           products: list, expected: list) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == expected
