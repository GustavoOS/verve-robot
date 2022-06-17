from time import sleep

from __init__ import *
from article import mount_article
from utill import get_title_tags
from web.pensador import get_quote_link


def fetch_info(content):
    result = parser.parse(content)
    title = result['title']
    result['link'] = youtube.search(f"verve {title}")
    result['images'] = finder.find_image(title)
    try:
        result['quote'] = citation.find_quote(title)
        reference_count = len(result['references'])
        link = get_quote_link(result['title']).split("www.")[1]
        result['references'].append(f"[{reference_count + 1}] {link}")
    except:
        result['quote'] = "Inserir citação aqui."

    return result


# Test
file = open("input.html", "r")
content = file.read()
file.close()
result = fetch_info(content)
article = mount_article(result)

verve.log_in()
verve.open_edit_panel()
verve.click_to_duplicate()
verve.open_inline_edit_options()
verve.fill_inline_edit_options(
    result['title'], get_title_tags(result['title']) +
    ", Cientista, verve, verve científica")
verve.open_edit_page()
verve.fill_page(article)
verve.change_outstand_image(result['link']['img'])
verve.define_seo(result["title"], result["link"]["seo"])

sleep(30)
