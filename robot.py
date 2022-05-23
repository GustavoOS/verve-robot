# selenium 4

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.action_chains import ActionChains

def fill_input(selector, text):
    el = driver.find_element(By.CSS_SELECTOR, f"input{selector}")
    el.send_keys(str(text))

def click_element(selector):
    el = driver.find_element(By.CSS_SELECTOR, selector)
    el.click()

def move_mouse(arg):
    print("Moving the cursor to the element")
    action = ActionChains(driver)
    action.move_to_element(driver.find_element(By.CSS_SELECTOR, arg)).perform()
    print("Cursor moved to the element")



driver = webdriver.Chrome(service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.implicitly_wait(30)
driver.get("https://vervecientifica.com.br/wp-admin")
fill_input("[type='text']", "verve.colab3@gmail.com")
fill_input("[type='password']", "njo#g$mmESAvtgGd$NS4noOh")
click_element("input[type='submit']")
driver.get("https://vervecientifica.com.br/wp-admin/edit.php")
driver.maximize_window()
move_mouse("tbody#the-list tr:nth-child(2)")
click_element("tbody#the-list tr:nth-child(2) a[title='Duplicar comodraft']")
move_mouse("tbody#the-list tr:nth-child(1)")
click_element("tbody#the-list tr:nth-child(1) button.editinline")

