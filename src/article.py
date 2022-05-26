from jinja2 import Environment, FileSystemLoader


def mount_article(result):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('article.jinja')
    return template.render(
        title= result['title'],
        link=result['link'],
        paragraphs=result['body'],
        references=result['references'],
        images=result['images'],
        quote=result['quote'])
