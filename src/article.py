import os

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

load_dotenv()
TEMPLATES = os.getenv('TEMPLATES')

def mount_article(result):
    env = Environment(loader=FileSystemLoader(TEMPLATES))
    template = env.get_template('article.jinja')
    return template.render(
        title= result['title'],
        link=result['link']['url'],
        paragraphs=result['body'],
        references=result['references'],
        images=result['images'],
        quote=result['quote'])
