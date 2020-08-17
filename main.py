import os
import logging
import json

import requests
import marshmallow
import jmespath


#TODO: Change to flask with simple form
def run():
    if url:
        while True:
            get_books_by_title(get_title())


def get_title() -> str:
    while True:
        title = input("Enter book title \n")
        print(f"Are u sure u provided correct title? \n {title}")
        is_title_valid = input("Enter Y/N \n")
        if is_title_valid in ["Y", 'y']:
            return title
        elif is_title_valid in ["n", "N"]:
            continue


def get_books_by_title(title: str) -> "Response":
    """Use GET request to get list of books from google - books api
    intitle - special keyword from google API  Returns results where
    the text following this keyword is found in the title."""

    params = {"q": "intitle:" + title,
              'maxResults': 5}
    resp = requests.get(url=url, params=params)
    print(json.dumps(json.loads(resp.content)))
    return resp


def use_jmespath_query(data, query):
    """Specify how to extract elements from JSON document"""
    jmespath.search(query, data)


if __name__ == "__main__":
    url = os.getenv("GOOGLE_API_URL")
    run()
