from time import sleep

from __init__ import *
from article import mount_article
from web.wikimedia import WikiMedia



def fetch_info(content):
    result = parser.parse(content)
    result['link'] = youtube.search(f"verve {result['title']}")
    result['images'] = finder.find_image(result['title'])
    return result


# verve.log_in()
# verve.open_edit_panel()
# verve.click_to_duplicate()
# verve.open_inline_edit_options()

# Test
file = open("input.html", "r")
content = file.read()
file.close()
result = fetch_info(content)
print(mount_article(result))

sleep(30)
