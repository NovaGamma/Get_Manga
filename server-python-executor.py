from flask import Flask,render_template, request
import subprocess

def validate_url(url):
    websites = ["isekaiscanmanga", "mangakakalot_tv", "mangakakalot", "mangatx", "towerofgod"]
    site = url.lower().replace("https://", "")
    if (site[0] == 'w'):
        site = site.split(".")[1] + "_tv"
    site = site.split("/")[0]

    if (" " in url != -1 or site in websites == -1):
        return False
    else:
        return True

def execute_command(url):
    subprocess.call("dir", shell=True)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def executor():
    if request.method == "POST":
        url = request.form["url"]
        if validate_url(url):
            execute_command(url)
        else:
            print("Wrong URL!")
    return render_template("command_executor.html")

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5001)
