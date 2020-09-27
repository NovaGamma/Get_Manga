import os
for number in range(2,18):
    try:
        chapter = []
        chapter2 = []
        for item in os.listdir():
            if "Chapter" in item:
                if item.split(' ')[1] == str(number):
                    chapter.append(item)
                elif item.split(' ')[1] == str(number)+'_1':
                    chapter2.append(item)
        n = 0
        n2 = 0
        print(len(chapter))
        print(len(chapter2))
        for page in chapter:
            if os.path.getsize(page) == 48378:
                n += 1
        for page in chapter2:
            if os.path.getsize(page) == 48378:
                n2 += 1
        if n > n2:
            for i in range(len(chapter)):
                os.remove(chapter[i])
                os.rename(chapter2[i],chapter[i])
        elif n <= n2:
            for i in range(len(chapter)):
                os.remove(chapter2[i])
    except:
        pass
