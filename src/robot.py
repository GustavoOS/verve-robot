import os
import pathlib
from pprint import pprint
from sys import platform
from time import sleep

from __init__ import *
from article import mount_article
from browser import Browser
from web.verve import VerveWebsite
from web.wikimedia import WikiMedia
from web.youtube import YoutubeWebsite
from parser import Parser
from util import get_title_tags
from web.pensador import Pensador, get_quote_link


SLASH = "\\" if platform == "win32" else "/"


class Robot:
    def __init__(self):
        self.browser = Browser()
        self.verve = VerveWebsite(self.browser)
        self.youtube = YoutubeWebsite(self.browser)
        self.parser = Parser()
        self.finder = WikiMedia(self.browser)
        self.citation = Pensador()

    def fetch_info(self, content):
        result = self.parser.parse(content)
        title = result['title']
        result['link'] = self.youtube.search(f"verve {title}")
        self.fetch_images(result, title)
        try:
            result['quote'] = self.citation.find_quote(title)
            reference_count = len(result['references'])
            link = get_quote_link(result['title']).split("www.")[1]
            result['references'].append(f"[{reference_count + 1}] {link}")
        except Exception as e:
            result['quote'] = "Inserir citação aqui."
        return result

    def fetch_images(self, result, title):
        try:
            result['images'] = self.finder.find_image(title)
        except:
            print("Imagem não encontrada para ", title)
            result['images'] = [
                "https://telhafer.com.br/image/no_image.jpg",
                "https://telhafer.com.br/image/no_image.jpg"
            ]

    def create_draft(self, result, article):
        self.verve.log_in()
        self.verve.open_edit_panel()
        self.verve.click_to_duplicate()
        self.verve.open_inline_edit_options()
        self.verve.fill_inline_edit_options(
            result['title'], get_title_tags(result['title']) +
            ", Cientista, verve, verve científica")
        self.verve.open_edit_page()
        self.verve.fill_page(article)
        self.verve.change_outstand_image(result['link']['img'])
        self.verve.define_seo(result["title"], result["link"]["seo"])

    def run(self, filename):
        file = open(filename, "r")
        content = file.read()
        file.close()
        result = self.fetch_info(content)
        article = mount_article(result)
        self.create_draft(result, article)
        self.browser.close()


def process_article(filename):
    robot = Robot()
    robot.run(filename)


# process_article("input.html")

# sleep(30)

directory = str(pathlib.Path().resolve()) + SLASH + "converted"
files = sorted(list(map(lambda t: t[2], os.walk(directory)))[0])
files = (list(filter(lambda file: file.split(".")[1].lower() == "html", files)))
if(len(files) == 0):
    raise Exception(f"There were no HTML files in directory {directory} .")

for file in files:
    print("Processing ", file)
    process_article(directory + SLASH + file)
    print("-"*30)


