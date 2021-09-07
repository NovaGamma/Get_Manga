import os

list = {}
for file in os.listdir('survival-story-of-a-sword-king-in-a-fantasy-world/'):
    nChapter = file.split(' ')[1]
    if nChapter in list.keys():
        list[nChapter].append(file)
    else:
        list[nChapter] = [file]
for key, item in list.items():
    if not os.path.exists(f'survival-story-of-a-sword-king-in-a-fantasy-world/Chapter {key}'):
        os.mkdir(f'survival-story-of-a-sword-king-in-a-fantasy-world/Chapter {key}')
    for file in item:
        print(item)
        nPage = file.split(' ')[-1]
        os.rename('survival-story-of-a-sword-king-in-a-fantasy-world/'+file,f'survival-story-of-a-sword-king-in-a-fantasy-world/Chapter {key}/page {nPage}')
