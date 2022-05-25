from browser import Browser
import urllib.parse


class YoutubeWebsite:
    def __init__(self, browser: Browser):
        self.browser = browser

    def search(self, name: str):
        param = urllib.parse.quote("verve " + name)
        self.browser.go_to_site(
            f"https://www.youtube.com/results?search_query={param}")
