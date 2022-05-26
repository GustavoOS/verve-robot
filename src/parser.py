from bs4 import BeautifulSoup, Tag


class Parser:
    result = {}

    def parse(self, doc: str):
        self.soup = BeautifulSoup(doc, 'html.parser')
        self.extract_title()
        self.get_references(self.soup.find_all('p'))
        self.result['body'] = self.soup.find_all('p')
        return self.result

    def extract_title(self):
        title = self.soup.find('p')
        split = title.get_text().split("(")
        self.result['title'] = split[0].strip().title()
        self.result['years'] = split[1][:-1].strip()
        title.extract()

    def get_references(self, paragraphs):
        p_text = list(map(lambda p: p.get_text().strip(), paragraphs))
        index = p_text.index("Referências:")
        for p in paragraphs[index:]:
            p.extract()
        self.result['references'] = p_text[index + 1:]
