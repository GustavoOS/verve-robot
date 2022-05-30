from functools import reduce


def get_title_tags(title: str):
    tags = set()
    full_names = title.split("/")
    for full_name in full_names:
        tags.add(full_name.strip())
        name = full_name.strip().split(" ")
        tags.add(name[-1])
        tags.add(f"{name[0]} {name[-1]}")
    return reduce(lambda a, b: f"{a}, {b}",list(tags))
