import flask
from flask import redirect,url_for,Flask,jsonify,render_template
import os

app = Flask(__name__)

@app.route('/chapter/<int:number>/page/<int:page_number>')
def pages(number,page_number):
    return flask.send_file(f"static/I'm The Great Immortal/Chapter {number} page {page_number}.png")

@app.route('/chapter/<int:number>')
def chapter(number):
    return render_template('text.html',number = number)

@app.route("/chapterlen/<int:number>")
def chapterlen(number):
    print(number)
    list = [page for page in os.listdir("static/I'm The Great Immortal") if page.startswith(f"Chapter {number} ")]
    return str(len(list))

@app.route('/get_list')
def list():
    list_dir = os.listdir('static/')
    manga_list = []
    for dir in list_dir:
        maxChapter = max([int(n.split(' ')[1]) for n in os.listdir('static/'+dir+'/')])
        manga_list.append(f"{dir}:{maxChapter}")
    response = "|".join(manga_list)
    return response

@app.route('/list')
def display_list():
    return render_template('list.html')

@app.route('/')
def main():
    return redirect(url_for('chapter',number=1))
    return render_template('test.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
