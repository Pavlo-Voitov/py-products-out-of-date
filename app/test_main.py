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
            datetime.date(2022, 2, 2),
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 10), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
            ],
            [],
        ),
        (
            datetime.date(2022, 2, 10),
            [
                {"name": "salmon", "expiration_date":
                    datetime.date(2022, 2, 1), "price": 600},
                {"name": "chicken", "expiration_date":
                    datetime.date(2022, 2, 5), "price": 120},
            ],
            ["salmon", "chicken"],
        ),
        (datetime.date(2022, 2, 2), [], []),
    ],
)
def test_outdated_products(today_date: datetime,
                           products: list, expected: list) -> None:
    with patch("app.main.datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        assert outdated_products(products) == expected
