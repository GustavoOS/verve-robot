from browser import Browser
import urllib.parse


class YoutubeWebsite:
    def __init__(self, browser: Browser):
        self.browser = browser

    def search(self, name: str):
        param = urllib.parse.quote(name)
        self.browser.go_to_site(
            f"https://www.youtube.com/results?search_query={param}")
        return transform_url_style(
            self.browser.get_anchor_href("#video-title"))


def transform_url_style(url: str):
    code = url.split("?v=")[1]
    return f"https://youtu.be/{code}"
