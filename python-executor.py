import sys
import subprocess

try:
    website = sys.argv[2]
    path = sys.argv[3]
except:
    print("Error, not enough arguments...")


if website == "isekaiscanmanga":
    cmd = 'python isekaiscanmanga.py '
elif website == "mangakakalot_tv":
    cmd = 'python mangakakalot_tv.py '
elif website == "mangakakalot":
    cmd = 'python mangakakalot.py '
elif website == "mangatx":
    cmd = 'python mangatx.py '
elif website == "towerofgod":
    cmd = 'python towerofgod.py '
else:
    print("Error trying to read the website...")
    sys.exit()

cmd += path
subprocess.call(cmd, shell=True)