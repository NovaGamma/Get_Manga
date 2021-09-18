from flask import redirect, url_for, Flask, render_template, send_file
import os
import json


def get_list_chapter(path):
    list_chapters = [chapter.lstrip('Chapter ') for chapter in os.listdir(f"static/manga/{path}/")]
    list_chapters2 = [chapter.replace('-', '.') for chapter in list_chapters]
    list_chapter_sorted = [float(chapter) if '.' in chapter else int(chapter) for chapter in list_chapters2]
    list_chapter_sorted.sort()
    list_chapter_sorted = [str(chapter) for chapter in list_chapter_sorted]
    return list_chapter_sorted


app = Flask(__name__)


@app.route('/<string:name>/chapter/<string:number>')
def manga(name, number):
    list_chapters = get_list_chapter(name)
    if '-' in number:
        number = number.replace('-', '.')
    index = list_chapters.index(number)
    number = number.replace('.', '-')
    if index == 0:
        previous_chapter = number
    else:
        previous_chapter = list_chapters[index - 1].replace('.', '-')
    if index == len(list_chapters) - 1:
        next_chapter = number
    else:
        next_chapter = list_chapters[index + 1].replace('.', '-')
    return render_template('manga.html', name=name, previous_chapter=previous_chapter,
                           current_chapter=number, next_chapter=next_chapter)


@app.route('/<string:name>/')
def reroute(name):
    if name in os.listdir('static/manga/'):
        first_chapter = os.listdir(f'static/manga/{name}/')[0].split(' ')[1]
        return redirect(url_for('manga', name=name, number=first_chapter))
    else:
        return f'Error : Manga {name} not found'


@app.route('/<string:name>/chapter/<string:number>/page/<int:page_number>')
def pages(name, number, page_number):
    if name in os.listdir('static/manga/'):
        return send_file(f"static/manga/{name}/Chapter {number}/page {page_number}.png")
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


@app.route("/<string:name>/chapterlen/<string:number>")
def chapterlen(name, number):
    if name in os.listdir('static/manga/'):
        if f'Chapter {number}' in os.listdir(f'static/manga/{name}/'):
            return str(len(os.listdir(f'static/manga/{name}/Chapter {number}')))
        else:
            return f"Chapter {number} not found"
    else:
        return f"Manga {name} not found"


@app.route('/get_list')
def list_manga():
    list_dir = os.listdir('static/manga/')
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
