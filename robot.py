from time import sleep
from __init__ import *
from parser import Parser

from article import mount_article


# verve.log_in()
# verve.open_edit_panel()
# verve.click_to_duplicate()
# verve.open_inline_edit_options()

# Test
parser = Parser()
file = open("input.html", "r")
content = file.read()
file.close()
result = parser.parse(content)
result['link'] = youtube.search(f"verve {result['title']}")
print(mount_article(result))

sleep(30)
