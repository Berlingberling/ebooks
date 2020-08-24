# -*- coding: utf-8 -*-

import os
from urllib import parse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MD_FILE = os.path.join(BASE_DIR, "README.md")
HEADER = "# 📚 目录"
TITLE = """

## {title}

"""
TEMPLATE = """
- [《{book_name}》]({book_path})
"""


def gen_conference(src_path):
    all_content = {}
    for root, dirs_name, file_names in os.walk(src_path):
        if ".git" in root or ".idea" in root or os.path.basename(root) == os.path.basename(BASE_DIR):
            print("skip {}".format(root))
            continue
        for file in file_names:
            dir_name = os.path.basename(root)
            path = "./{}/{}".format(dir_name, file)
            if all_content.get(dir_name) is None:
                all_content[dir_name] = [path]
            else:
                all_content[dir_name].append(path)
    with open(MD_FILE, "w+",encoding="utf-8") as md:
        md.write(HEADER)
        for index, key in enumerate(all_content):
            md.write(TITLE.format(title=key))
            for _, path in enumerate(all_content[key]):
                md.write(TEMPLATE.format(book_name=os.path.basename(path), book_path=parse.quote(path)))


if __name__ == '__main__':
    gen_conference(BASE_DIR)
