from time import sleep
from browser import Browser
from verve import VerveWebsite


browser = Browser()
verve = VerveWebsite(browser)

verve.log_in()
verve.open_edit_panel()
verve.click_to_duplicate()
verve.open_inline_edit_options()
sleep(30)
