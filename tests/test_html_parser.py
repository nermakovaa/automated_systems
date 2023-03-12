import pytest
import pandas as pd

from pandas.testing import assert_frame_equal
from datetime import datetime

from src.html.html_parser import parse_url


def convert_to_date(x):
    return datetime.strptime(x, "%Y-%m-%d %H:%M")


@pytest.mark.parametrize(
    "first_page, last_page, reference_table_path",
    [
        (1, 1, "./tests/reference/reference_table_1_1.csv")
    ]
)
def test_html_parser_valid(first_page, last_page, reference_table_path):
    parsed_table = parse_url(
        first_page=first_page,
        last_page=last_page,
        save_table=False
    )

    reference_table = pd.read_csv(reference_table_path, index_col="Unnamed: 0")
    reference_table["article_date"] = reference_table["article_date"].apply(convert_to_date)


    print(reference_table.article_date)
    print(parsed_table.article_date)

    assert_frame_equal(parsed_table, reference_table, check_like=True)


@pytest.mark.parametrize(
    "first_page, last_page",
    [
        (-1, 10),  # negative first_page
        (0, 10),  # zero first_page
        (1, 0),  # zero last_page
        (5, 3),  # last_page < first_page
        (2, -2),  # negative last_page
    ]
)
def test_html_parser_invalid(first_page, last_page):
    with pytest.raises(AssertionError):
        parse_url(
            first_page=first_page,
            last_page=last_page,
            save_table=False
            )