from flask import redirect,url_for,Flask,render_template, send_file, jsonify, request
from flask_cors import CORS, cross_origin
import os, json
from requestHandler import handler, checkUrl
from historyHandler import get_history, add_to_history
from difflib import SequenceMatcher

def get_list_chapter(path):
    list_chapters = [chapter.lstrip('Chapter ') for chapter in os.listdir(f"static/manga/{path}/")]
    list_chapters2 = [chapter.replace('-', '.') for chapter in list_chapters]
    list_chapter_sorted = [float(chapter) if '.' in chapter else int(chapter) for chapter in list_chapters2]
    list_chapter_sorted.sort()
    list_chapter_sorted = [str(chapter) for chapter in list_chapter_sorted]
    return list_chapter_sorted


app = Flask(__name__)
cors = CORS(app)

file = open('read.json','r')
reads = json.load(file)

@app.route('/<string:name>/chapter/<string:number>')
def manga(name, number):
    list_chapters = get_list_chapter(name)
    if '-' in number:
        number = number.replace('-', '.')
    index = list_chapters.index(number)
    if index == 0:
        previous_chapter = number
    else:
        previous_chapter = list_chapters[index - 1].replace('.', '-')
    if index == len(list_chapters) - 1:
        next_chapter = number
    else:
        next_chapter = list_chapters[index+1].replace('.','-')
    add_to_history(name,number)
    return render_template('manga.html',ip=ip,name=name,previous_chapter=previous_chapter,current_chapter=number,next_chapter=next_chapter)

@app.route('/<string:name>/')
def reroute(name):
    if name in os.listdir('static/manga/'):
        first_chapter = get_list_chapter(name)
        return redirect(url_for('manga', name=name, number=first_chapter[0]))
    else:
        return f'Error : Manga {name} not found'

@app.route('/<string:name>/chapterlist/')
def chapterlist(name):
    if name in os.listdir('static/manga/'):
        chapters = get_list_chapter(name)
        return jsonify(chapters)

@app.route('/history')
def history():
    history_dict = get_history()
    list = []
    for key,value in history_dict.items():
        list.append([key,value])
    return jsonify(list)

@app.route('/<string:name>/chapter/<string:number>/page/<int:page_number>')
def pages(name,number,page_number):
    if name in os.listdir('static/manga/') and f"Chapter {number}" in os.listdir(f'static/manga/{name}/'):
        list_pages = os.listdir(f"static/manga/{name}/Chapter {number}/")
        file_format = list_pages[int(page_number)-int(list_pages[0][5:-4])].split('.')[-1]
        print(f"static/manga/{name}/Chapter {number}/page {page_number}.{file_format}")
        return send_file(f"static/manga/{name}/Chapter {number}/page {page_number}.{file_format}")
    else:
        return f'page {page_number} not found'


@app.route('/<string:name>/preview')
def get_preview(name):
    if name in os.listdir('static/manga/'):
        first_chapter = os.listdir(f'static/manga/{name}/')[0]
        first_image = os.listdir(f'static/manga/{name}/{first_chapter}/')[0]
        return send_file(f'static/manga/{name}/{first_chapter}/{first_image}')
    else:
        return f'Error : Manga {name} not found'

@app.route("/request", methods=["POST"])
def get_request():
    data = request.get_json()
    return handler(data)

@app.route("/<string:name>/chapterlen/<string:number>")
def list_pages(name, number):
    if name in os.listdir('static/manga/'):
        if f'Chapter {number}' in os.listdir(f'static/manga/{name}/'):
            pages = [int(page[5:-4]) for page in os.listdir(f'static/manga/{name}/Chapter {number}')]
            pages.sort()
            return jsonify(pages)
        else:
            return f"Chapter {number} not found"
    else:
        return f"Manga {name} not found"


@app.route('/read', methods=["GET","POST"])
def is_read():
    name = request.get_json()

    for el in reads:
        el = el.rstrip('\n')
        seq = SequenceMatcher(None,el.lower(),name['title'].lower())
        if seq.ratio() > 0.8:
            return jsonify(1)
    return jsonify(0)


@app.route('/get_list')
def list_manga():
    list_dir = os.listdir('static/manga/')
    m_time = [(dir,os.stat('static/manga/'+dir)[8]) for dir in list_dir]
    result = sorted(m_time, key=lambda dir: dir[1])[::-1]
    clean = [item[0] for item in result]
    return json.dumps(clean)


@app.route('/list')
def display_list():
    return render_template('list.html',ip=ip)

@app.route('/url_check', methods=["POST"])
def check_url():
    url = request.get_json()['url']
    return jsonify(checkUrl(url))


@app.route('/')
def main():
    return redirect(url_for('display_list'))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    ip = '192.168.1.80'
    app.run(ip,threaded=True, port=5000)
