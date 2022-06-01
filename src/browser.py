from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


class Browser:
    def __init__(self):
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
        driver.implicitly_wait(30)
        self.driver = driver

    def fill_input(self, selector, text):
        el = self.driver.find_element(By.CSS_SELECTOR, selector)
        el.send_keys(str(text))

    def click_element(self, selector, n=0):
        el = self.driver.find_elements(By.CSS_SELECTOR, selector)
        el[n].click()

    def move_mouse(self, arg):
        print("Moving the cursor to the element")
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(
            By.CSS_SELECTOR, arg)).perform()
        print("Cursor moved to the element")

    def go_to_site(self, site):
        self.driver.get(site)

    def maximize(self):
        self.driver.maximize_window()

    def get_attribute(self, selector, attribute, index=0):
        el = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return el[index].get_attribute(attribute)

    def clear(self, selector):
        self.driver.find_element(By.CSS_SELECTOR, selector).clear()

    def clear_and_fill(self, selector, text):
        el = self.driver.find_element(By.CSS_SELECTOR, selector)
        el.clear()
        el.send_keys(text)

    def paste(self, selector):
        el = self.driver.find_element(By.CSS_SELECTOR, selector)
        el.send_keys(Keys.CONTROL, 'v')
