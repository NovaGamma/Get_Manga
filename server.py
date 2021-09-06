import flask
from flask import redirect,url_for,Flask,jsonify,render_template
import os

app = Flask(__name__)

@app.route('/<string:name>/chapter/<int:number>')
def manga(name,number):
    return render_template('manga.html',name=name,number=number)

@app.route('/<string:name>')
def reroute(name):
    if dir in os.listdir('static/'):
        #print(url_for('manga',name=name,chapter=1))
        url = f"http://127.0.0.1:5000/{name}/chapter/1"
        return redirect(url)

@app.route('/<string:name>/chapter/<int:number>/page/<int:page_number>')
def pages(name,number,page_number):
    for dir in os.listdir('static/'):
        copy = dir
        if dir == name:
            break
    return flask.send_file(f"static/{copy}/Chapter {number} page {page_number}.png")

@app.route('/chapter/<int:number>')
def chapter(number):
    return render_template('text.html',number = number)

@app.route("/<string:name>/chapterlen/<int:number>")
def chapterlen(name,number):
    for dir in os.listdir('static/'):
        copy = dir
        if dir.lower().replace(' ','_') == name:
            break
    list = [page for page in os.listdir(f"static/{copy}") if page.startswith(f"Chapter {number} ")]
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
    return redirect(url_for('display_list'))
    return render_template('test.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
