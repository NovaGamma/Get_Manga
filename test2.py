import os

def list():
    list_dir = os.listdir('static/')
    result = {}
    for dir in list_dir:
        maxChapter = max([int(n.split(' ')[1]) for n in os.listdir('static/'+dir+'/')])
        result[dir] = maxChapter
    return result

print(list())
