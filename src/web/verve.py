import os
from time import sleep

import pyperclip
from browser import Browser
from dotenv import load_dotenv

load_dotenv()
VERVE_LOGIN = os.getenv('VERVE_LOGIN')
VERVE_PASSWORD = os.getenv('VERVE_PASSWORD')


class VerveWebsite:
    def __init__(self, browser: Browser):
        self.browser = browser

    def log_in(self):
        self.browser.go_to_site("https://vervecientifica.com.br/wp-admin")
        self.browser.fill_input("input[type='text']", VERVE_LOGIN)
        self.browser.fill_input("input[type='password']", VERVE_PASSWORD)
        self.browser.click_element("input[type='submit']")

    def open_edit_panel(self):
        self.browser.go_to_site(
            "https://vervecientifica.com.br/wp-admin/edit.php")
        self.browser.maximize()

    def click_to_duplicate(self):
        self.browser.move_mouse("tbody#the-list tr:nth-child(2)")
        self.browser.click_element(
            "tbody#the-list tr:nth-child(2) a[title='Duplicar comodraft']")

    def open_inline_edit_options(self):
        print("open inline editor")
        self.browser.move_mouse("tbody#the-list tr:nth-child(1)")
        self.browser.click_element(
            "tbody#the-list tr:nth-child(1) button.editinline")

    def fill_inline_edit_options(self, title, tags):
        self.browser.clear_and_fill("input.ptitle", title)
        self.browser.clear_and_fill(
            "textarea[data-wp-taxonomy='post_tag']", tags)
        self.browser.click_element("button.save")

    def open_edit_page(self):
        url = self.browser.get_attribute(
            "tbody#the-list tr:nth-child(1) span.edit > a", "href")
        sleep(2)
        self.browser.go_to_site(url)
        self.browser.click_element("button[aria-label='Fechar janela']")
        self.browser.click_element("button[aria-label='Opções']")
        self.browser.click_element(
            ".components-menu-group:nth-child(2) button", -1)

    def fill_page(self, page: str):
        area = "textarea.editor-post-text-editor"
        sleep(1)
        self.browser.clear(area)
        pyperclip.copy(page)
        self.browser.paste(area)
