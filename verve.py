
from browser import Browser


class VerveWebsite:
    def __init__(self, browser: Browser):
        self.browser = browser

    def log_in(self):
        self.browser.go_to_site("https://vervecientifica.com.br/wp-admin")
        self.browser.fill_input("[type='text']", "verve.colab3@gmail.com")
        self.browser.fill_input("[type='password']",
                                "njo#g$mmESAvtgGd$NS4noOh")
        self.browser.click_element("input[type='submit']")

    def open_edit_panel(self):
        self.browser.go_to_site(
            "https://vervecientifica.com.br/wp-admin/edit.php")
        self.browser.maximize()

    def click_to_duplicate(self):
        self.browser.move_mouse("tbody#the-list tr:nth-child(2)")
        self.browser.click_element("tbody#the-list tr:nth-child(2) a[title='Duplicar comodraft']")

    def open_inline_edit_options(self):
        print("open inline editor")
        self.browser.move_mouse("tbody#the-list tr:nth-child(1)")
        self.browser.click_element(
            "tbody#the-list tr:nth-child(1) button.editinline")
