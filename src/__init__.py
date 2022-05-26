
from parser import Parser

from browser import Browser
from web.pensador import Pensador
from web.verve import VerveWebsite
from web.wikimedia import WikiMedia
from web.youtube import YoutubeWebsite

browser = Browser()
verve = VerveWebsite(browser)
youtube = YoutubeWebsite(browser)
parser = Parser()
finder = WikiMedia(browser)
citation = Pensador()
