from calendar import monthrange
from datetime import datetime

MONTH_MAP = {
    "января": 1,
    "февраля": 2,
    "марта": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12,
}


def convert_to_datetime(date, time):
    # format {day} {month}
    if len(date.split()) == 2:
        day, month_str = date.split()
        day = int(day)
        year = None
    # format {day} {month} {year}
    elif len(date.split()) == 3:
        day, month_str, year = date.split()
        day = int(day)
        year = int(year)
    else:
        raise TypeError(f"Unexpected date: {date}")

    assert month_str in MONTH_MAP, "Incorrect month parsed"
    if year:
        assert year <= datetime.now().year, "Incorrect year parsed"
    else:
        year = datetime.now().year

    month = MONTH_MAP[month_str]
    month_days = monthrange(year, month)[1]
    assert 1 <= day <= month_days, "Incorrect day parsed"

    hour, minute = map(int, time.split(":"))

    assert 0 <= hour <= 23, "Incorrect hour"
    assert 0 <= minute <= 59, "Incorrect minute"

    datetime_str = f"{day}/{month:02d}/{year} {hour}:{minute:02d}"
    datetime_object = datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")

    return datetime_object
