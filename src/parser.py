from bs4 import BeautifulSoup


class Parser:
    result = {}

    def parse(self, doc: str):
        self.soup = BeautifulSoup(doc, 'html.parser')
        self.extract_title()
        self.get_references(self.soup.find_all('p'))
        self.extract_paragraphs()
        return self.result

    def extract_title(self):
        title = self.soup.find('p')
        split = title.get_text().split("(")
        self.result['title'] = split[0].strip().title()
        self.result['years'] = split[1][:-1].strip()
        title.extract()

    def get_references(self, paragraphs):
        p_text = list(map(lambda p: p.get_text().strip(), paragraphs))
        try:
            index = p_text.index("Referências:")
            for p in paragraphs[index:]:
                p.extract()
            self.result['references'] = p_text[index + 1:]
        except:
            self.result['references'] = ["* Sem referências"]

    def extract_paragraphs(self):
        self.result['body'] = list(
            map(lambda el: el.get_text().strip().replace("\n", "").replace("  ", " "), self.soup.find_all('p')))
