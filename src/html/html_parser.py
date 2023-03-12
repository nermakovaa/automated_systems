from collections import defaultdict
from os.path import join
from time import sleep

import pandas as pd
import requests
from bs4 import BeautifulSoup as BS

from ..date_parser import convert_to_datetime

URL = "https://knife.media/category/news/"


def parse_url(first_page, last_page, save_table=True):
    parsed_dict = defaultdict(list)

    assert first_page > 0, "Page must be a positive integer"
    assert last_page >= first_page, "Last page must be not less than first page"

    for page in range(first_page, last_page + 1):
        page_url = join(URL, f"page/{page}")
        req = requests.get(page_url)
        soup = BS(req.text, "lxml")

        titles = soup.findAll("div", class_="widget-news__wrapper")

        for title in titles:
            article_title = title.find("a", class_="widget-news__content-link").text
            article_link = title.find("a", class_="widget-news__content-link").get(
                "href"
            )
            article_time = title.find("span", class_="meta__item").text
            article_date = title.findAll("span", class_="meta__item")[1].text

            article_datetime = convert_to_datetime(article_date, article_time)

            parsed_dict["article_title"].append(article_title)
            parsed_dict["article_link"].append(article_link)
            parsed_dict["article_date"].append(article_datetime)
            parsed_dict["page"].append(page)

    table = pd.DataFrame(parsed_dict)
    if save_table:
        table.to_csv(f"pages {first_page} - {last_page}.csv")

    return table


parse_url(1, 1)