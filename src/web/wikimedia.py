import urllib.parse
from browser import Browser


class WikiMedia:
    def __init__(self, browser: Browser):
        self.browser = browser

    def find_image(self, name):
        param = urllib.parse.quote(name)
        result = []
        for selector in ['a.sdms-image-result--portrait', 'a.sdms-image-result']:
            result.append(self.get_image_from_search(param, selector))
        return result

    def get_image_from_search(self, param, selector):
        self.browser.go_to_site(
            f"https://commons.wikimedia.org/w/index.php?search={param}" +
            "&title=Special:MediaSearch&go=Go&type=image&uselang=pt-br")
        self.browser.click_element(selector)
        return self.browser.get_attribute("div.fullMedia > p > a", "href")
