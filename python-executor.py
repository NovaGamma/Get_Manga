import sys
import subprocess

try:
    website = sys.argv[2]
    path = sys.argv[3]
except:
    print("Error, not enough arguments...")


if website == "https://mangatx.com/manga/":
    cmd = 'python mangatx.py '
elif website == "https://www.asurascans.com/":
    cmd = 'python asurascans.py '
elif website == "https://reaperscans.com/series/":
    cmd = 'python reaperscans.py '
elif website == "https://isekaiscanmanga.com/manga/":
    cmd = 'python isekaiscanmanga.py '
elif website == "https://readmanganato.com/manga":
    cmd = 'python mangakakalot.py '
elif website == "https://ww1.mangakakalot.tv/chapter/manga":
    cmd = 'python mangakakalot_tv.py '
else:
    print("Error trying to read the website...")
    sys.exit()

cmd += path
subprocess.call(cmd, shell=True)
