from typing import Dict

import requests
import os
from bs4 import BeautifulSoup
import sys
import time
import importlib
import shutil


def main(path):
    SITE_LIST = {
        'mangatx.com': 'mangatx',
        'isekaiscanmanga.com': 'isekaiscanmanga',
        'mangakakalot.com': 'mangakakalot',
        'ww.mangakakalot.tv': 'mangakakalot_tv'
        }
    module = importlib.import_module(SITE_LIST[path.split('/')[2]])
    name = module.get_name(path)

    dirName = f"static/manga/{name}"
    if not(os.path.exists(dirName)):
        os.mkdir(dirName)
    r = requests.get(path)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = module.get_chapter_list(soup)  # -> sort the chapter list in the function (depending on the site)
    print('Found {} chapters !'.format(len(result)))
    # maybe add a function to only download certain chapters, like from the 15th one or smt
    for chapter in result:
        t0 = time.time()
        url = module.get_chapter_url(chapter)
        chapter_number = module.get_chapter_number(chapter)  # chapter or url as parameter -> to decide
        print(chapter_number)
        chapter_request = requests.get(url)
        chapter_soup = BeautifulSoup(chapter_request.text, 'html.parser')
        pages = module.get_pages(chapter_soup)
        if not os.path.exists(f"{dirName}/Chapter {chapter_number}/"):
            os.mkdir(f"{dirName}/Chapter {chapter_number}/")
        headers = module.get_headers()
        for page in pages:
            page_url = page[1]
            image_name = dirName+"/Chapter "+str(chapter_number)+'/page '+str(int(page[0])+1)+".png"
            if not os.path.exists(image_name):
                image = requests.get(page_url, headers=headers)
                if image.status_code == 404:
                    retry = 0
                    while image.status_code == 404 and retry < 20:
                        time.sleep(1)
                        image = requests.get(page_url, headers=headers)
                        retry += 1
                    if retry == 20:
                        print(f"error 404 {page_url}\n{image}")
                        shutil.copyfile('static/empty_image.png', image_name)
                        continue
                with open(image_name, 'wb') as f:
                    f.write(image.content)
        t1 = time.time()
        sys.stdout.write(f"{t1-t0} s\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "https://mangatx.com/manga/im-not-the-overlord/chapter-9/"
    main(path)
