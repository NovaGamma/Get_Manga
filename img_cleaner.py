import os
from PIL import Image
import threading

class Thread(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path = path

    def run(self):
        path = self.path
        counter = 0
        sum = 0
        for chapter in os.listdir(path):
            avg = 0
            sub_counter = 0
            for image in os.listdir(f'{path}/{chapter}/'):
                counter += 1
                sub_counter += 1
                img = Image.open(f'{path}/{chapter}/{image}')
                sum += img.size[0]
                avg += img.size[0]
        new_size = int(sum/counter)

        for chapter in os.listdir(f'{path}/'):
            print(path,chapter)
            for image in os.listdir(f'{path}/{chapter}/'):
                img = Image.open(f'{path}/{chapter}/{image}')
                if img.size[0] != new_size:
                    ratio = int(img.size[1] / img.size[0])
                    if ratio == 0:
                        ratio = 1
                    if img.size[0] / new_size == 2:
                        size = 2
                    else:
                        size = 1
                    resized = img.resize((new_size*size,new_size*ratio))
                    resized.save(f'{path}/{chapter}/{image}')

list_thread = []
for manga in os.listdir('static/manga/'):
    list_thread.append(Thread(f'static/manga/{manga}'))

for thread in list_thread:
    thread.start()
