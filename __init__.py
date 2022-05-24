from browser import Browser
from verve import VerveWebsite
from youtube import YoutubeWebsite


browser = Browser()
verve = VerveWebsite(browser)
youtube = YoutubeWebsite(browser)
