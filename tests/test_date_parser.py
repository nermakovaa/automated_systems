import pytest
from datetime import datetime

from src.date_parser import convert_to_datetime
from src.html.html_parser import parse_url


@pytest.mark.parametrize(
    "date, time, expected",
    [
        ("20 января 2023", "14:45", "20/01/2023 14:45"),
        ("12 июля 2022", "20:21", "12/07/2022 20:21"), 
        ("1 мая 2020", "22:00", "01/05/2020 22:00"),
        ("01 мая 2020", "22:00", "01/05/2020 22:00"),
        ("12 сентября 2013", "10:00", "12/09/2013 10:00")
    ]
)
def test_date_parser_valid_date(date, time, expected):
    output = convert_to_datetime(date, time)
    expected = datetime.strptime(expected, "%d/%m/%Y %H:%M")
    assert output == expected


@pytest.mark.parametrize(
    "date, time",
    [
        ("22 декабря 2024", "10:10"),  # 2024 > current year (2023)
        ("30 февраля 2023", "09:33"),  # Feb 30 doesn't exist
        ("17 сентября 2018", "25:33"),  # 25 hours
        ("15 апреля 2020", "24:61"),  # 24 hours, 61 minutes
        ("9 майя 2021", "16:03"),  # invalid month
    ]    
)
def test_date_parses_invalid_date(date, time):
    with pytest.raises(AssertionError):
         convert_to_datetime(date, time)
