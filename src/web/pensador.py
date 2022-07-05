import traceback
import urllib.parse

import requests
from bs4 import BeautifulSoup


class Pensador:

    def find_quote(self, author: str):
        site = get(get_quote_link(author))
        self.soup = BeautifulSoup(site, 'html.parser')
        self.extract_quotes()
        quote = self.select_quote(author)
        print("quote is ", quote)
        return quote

    def extract_quotes(self):
        authors = self.get_elements_inner_text('.phrases-list .autor a')
        shares = self.get_elements_inner_text('.phrases-list .total-shares')
        quotes = self.get_elements_inner_text('.phrases-list .frase')
        self.quotes = []
        for i in range(len(authors)):
            self.quotes.append(
                {
                    'author': authors[i].strip(),
                    'shares': self.parse_shares(shares, i),
                    'quote': quotes[i].strip().replace("\n", "")
                }
            )

    def parse_shares(self, shares, i):
        try:
            return self.parse_int(shares[i])
        except:
            print("Error fetching phrase")
            traceback.print_exc()
            return 0

    def parse_int(self, number):
        text = number.strip().split(" ")[0]
        splited = text.split(".")
        if len(splited) > 1:
            return int(f"{splited[0]}{splited[1]}00")
        return int(text)

    def get_elements_inner_text(self, selector):
        result = self.soup.select(selector)
        return list(map(lambda el: el.get_text(), result))

    def select_quote(self, author: str):
        self.quotes = list(
            filter(lambda q: q['author'].lower() == author.lower()
                   and q['shares'] > 0, self.quotes))
        if len(self.quotes) == 0:
            raise Exception(f"No quotes were found for {author}")
        self.quotes.sort(key=lambda q: q['shares'], reverse=True)
        return self.quotes[0]['quote']


def get(url):
    res = requests.get(url, allow_redirects=True)
    res.raise_for_status()
    return res.text


def get_quote_link(author):
    param = urllib.parse.quote(author)
    url = f"https://www.pensador.com/busca.php?q={param}"
    return url
