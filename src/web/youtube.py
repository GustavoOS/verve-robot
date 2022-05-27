import urllib.parse

import requests
from browser import Browser


class YoutubeWebsite:
    def __init__(self, browser: Browser):
        self.browser = browser

    def search(self, name: str):
        param = urllib.parse.quote(name)
        self.browser.go_to_site(
            f"https://www.youtube.com/results?search_query={param}")
        img_src = self.browser.get_attribute(
            "#img", 'src', 1).split("?")[0].strip()
        return {
            'img': download_image(name, img_src),
            'url': transform_url_style(
                self.browser.get_attribute("a#video-title", 'href'))}


def transform_url_style(url: str):
    code = url.split("?v=")[1]
    return f"https://youtu.be/{code}"


def make_file_name(name: str, src: str):
    extension = src.split(".")[-1].strip()
    format_name = name.lower().replace(" ", "_")
    return f"{format_name}.{extension}"


def download_image(name: str, src: str):
    dir_name = f"../images/{make_file_name(name, src)}"
    r = requests.get(src, allow_redirects=True)
    open(dir_name, 'wb').write(r.content)
    return dir_name
