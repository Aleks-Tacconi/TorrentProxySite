from typing import List
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, Tag


class WebScraper:
    def __init__(self, url: str) -> None:
        self.__url = url

    def __hrefs(self) -> List[str]:
        try:
            response = requests.get(self.__url, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")

            return [
                str(link.get("href"))
                for link in soup.find_all("a", href=True)
                if isinstance(link, Tag)
            ]
        except requests.exceptions.ConnectTimeout:
            return []

    def find_all(self) -> List[str]:
        hrefs = self.__hrefs()
        hrefs = [urljoin(self.__url, href) for href in hrefs]

        return hrefs

    def find_tags(self, tag: str) -> List[str]:
        try:
            response = requests.get(self.__url, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")

            return [t.get_text(strip=True) for t in soup.find_all(tag)]
        except requests.exceptions.ConnectTimeout:
            return []

    def find_first_tag(self, tag: str) -> str:
        try:
            response = requests.get(self.__url, timeout=20)
            soup = BeautifulSoup(response.text, "html.parser")
            result = soup.find(tag)

            return result.get_text(strip=True) if result else ""
        except requests.exceptions.ConnectTimeout:
            return ""
