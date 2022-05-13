import os
import json
import requests
import sys
import subprocess

sites = [
'https://mangatx.com/manga/',
'https://isekaiscanmanga.com/manga/',
'https://www.asurascans.com/',
'https://reaperscans.com/series/',
'https://readmanganato.com/manga',
'https://mangakakalot.com/chapter/',
'https://ww3.mangakakalot.tv/chapter/manga',
]

def checkUrl(url):
    for template in sites:
        if url.startswith(template):
            return 'OK'
    return 'NO'

def handler(data):
    print(data)
    url = data['url']
    chapter = data['chapter']
    result = [[url,template] for template in sites if url.startswith(template)]
    path,website = result[0]

    if website == "https://mangatx.com/manga/":
        cmd = 'python mangatx.py '
    elif website == "https://www.asurascans.com/":
        cmd = 'python asurascans.py '
    elif website == "https://reaperscans.com/series/":
        cmd = 'python reaperscans.py '
    elif website == "https://isekaiscanmanga.com/manga/":
        cmd = 'python isekaiscanmanga.py '
    elif website == "https://readmanganato.com/manga":
        cmd = 'python manganato.py '
    elif website == "https://mangakakalot.com/chapter/":
        cmd = 'python mangakakalot.py '
    elif website == "https://ww3.mangakakalot.tv/chapter/manga":
        cmd = 'python mangakakalot_tv.py '
    else:
        print("Error trying to read the website...")
        sys.exit()

    cmd += path
    cmd += f" {chapter}"
    subprocess.call(cmd, shell=True)

    return 'OK' if len(result) == 1 else 'Error'
