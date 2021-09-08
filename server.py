from flask import redirect,url_for,Flask,render_template, send_file
import os
import json

app = Flask(__name__)

@app.route('/<string:name>/chapter/<int:number>')
def manga(name,number):
    return render_template('manga.html',name=name,number=number)

@app.route('/<string:name>/')
def reroute(name):
    if name in os.listdir('static/'):
        first_chapter = os.listdir(f'static/{name}/')[0].split(' ')[1]
        return redirect(url_for('manga',name=name,number=int(first_chapter)))
    else:
        return f'Error : Manga {name} not found'

@app.route('/<string:name>/chapter/<int:number>/page/<int:page_number>')
def pages(name,number,page_number):
    if name in os.listdir('static/'):
        return send_file(f"static/{name}/Chapter {number}/page {page_number}.png")
    else:
        return f'page {page_number} not found'

@app.route('/<string:name>/preview')
def getPreview(name):
    if name in os.listdir('static/'):
        first_chapter = os.listdir(f'static/{name}/')[0]
        first_image = os.listdir(f'static/{name}/{first_chapter}/')[0]
        return send_file(f'static/{name}/{first_chapter}/{first_image}')
    else:
        return f'Error : Manga {name} not found'


@app.route("/<string:name>/chapterlen/<int:number>")
def chapterlen(name,number):
    if name in os.listdir('static/'):
        if f'Chapter {number}' in os.listdir(f'static/{name}/'):
            return str(len(os.listdir(f'static/{name}/Chapter {number}')))
        else:
            return f"Chapter {number} not found"
    else:
        return f"Manga {name} not found"

@app.route('/get_list')
def list():
    list_dir = os.listdir('static/')
    return json.dumps(list_dir)

@app.route('/list')
def display_list():
    return render_template('list.html')

@app.route('/')
def main():
    return redirect(url_for('display_list'))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
