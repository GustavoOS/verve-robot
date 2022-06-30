from browser import Browser


class WikiMedia:
    def __init__(self, browser: Browser):
        self.browser = browser

    def find_image(self, name):
        self.search(name)
        if self.browser.contains(".sdms-did-you-mean"):
            self.browser.click_element(".sdms-did-you-mean a")
        links = list(map(self.get_link, range(2)))
        links.reverse()
        return list(map(self.get_image_from_search, links))

    def search(self, name):
        self.browser.go_to_site(
            "https://commons.wikimedia.org/wiki/Main_Page?uselang=pt-br")
        self.browser.fill_input("input[name='search']", name)
        self.browser.click_element("input[name='go']")

    def get_image_from_search(self, link):
        self.browser.go_to_site(link)
        return self.browser.get_attribute("div.fullMedia > p > a", "href")

    def get_link(self, index):
        return self.browser.get_attribute("#sd-tab-image a[title]", "href", index)
