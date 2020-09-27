import os
import pygame

pygame.init()

def smaller(e1,e2):
    if e1[2] > e2[2]: #mean that the chapter number of e2 is smaller
        return e2
    elif e1[2] < e2[2]:
        return e1
    else:#mean that e1[2] == e2[2] hence chapter numbers are the same
        if int(e1[1]) > int(e2[1]):
            return e2
        else:
            return e1

def load_chapter(chapter_number,path = ''):#load in memory a whole chapter
    hold = []
    for page in os.listdir("Above All Gods/"):
        if 'Chapter' in page:
            temp = page.split(" ")
            if '-' in temp[1]:
                number = int(temp[1].split('-')[0])
            else:
                number = int(temp[1])
            if number == chapter_number:
                try:
                    img = pygame.image.load(path+page).convert()
                except:
                    img = pygame.image.load('broken.png').convert()
                hold.append([img,page.split(' ')[-1].split('.')[0],temp[1]])
    #sort hold
    sorted = []
    for i in range(len(hold)):
        temp = hold[0]
        for e in hold:
            temp = smaller(temp,e)
        sorted.append(temp)
        hold.remove(temp)
    chapter = []
    for page in sorted:
        if len(chapter) > 0:
            chapter.append([page[0],chapter[-1][0].get_height() + chapter[-1][1],page[0]])
        else:
            chapter.append([page[0],0,page[0]])
    return chapter

screenx = 1240
screeny = 980

screen=pygame.display.set_mode((screenx,screeny),pygame.RESIZABLE)
path_origin = "Download/"
name = path_origin + "The Great Ruler"
y=10
scroll_y = 0
scalling = 5
chapter_number = 1
chapter = load_chapter(chapter_number,name+'/')
pygame.display.set_caption(name+" Chapter "+str(chapter_number))
while True:
    #pygame.VIDEORESIZE event
    for img in chapter:
        screen.blit(img[0],((screenx - img[0].get_width())/2,img[1] + scroll_y))
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            scroll_y-=50
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            chapter_number += 1
            scroll_y = 0
            chapter = load_chapter(chapter_number,name+'/')
            pygame.display.set_caption(name+" Chapter "+str(chapter_number))
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            chapter_number -= 1
            scroll_y = 0
            chapter = load_chapter(chapter_number,name+'/')
            pygame.display.set_caption(name+" Chapter "+str(chapter_number))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and keys[pygame.K_LCTRL]:
                temp = 0
                for img in chapter:
                    calcul = int(round(img[0].get_height()*(scalling/100))/2)
                    img[1] = img[1] + calcul
                    temp_img = img[2]
                    img[0] = pygame.transform.smoothscale(img[2],(img[0].get_width() + int(round(img[0].get_width()*(scalling/100))),img[0].get_height() + int(round(img[0].get_height()*(scalling/100)))))
                    img[2] = temp_img
                    screen.fill(color = (255,255,255))
            elif event.button == 4:
                scroll_y += 50
            if event.button == 5 and keys[pygame.K_LCTRL]:
                for img in chapter:
                    img[1] = img[1] - int(round(img[0].get_height()*(scalling/100))/2)
                    img[0] = pygame.transform.smoothscale(img[2],(img[0].get_width() - int(round(img[0].get_width()*(scalling/100))),img[0].get_height() - int(round(img[0].get_height()*(scalling/100)))))
                    screen.fill(color = (255,255,255))
            elif event.button == 5:
                scroll_y -= 50
        elif event.type == pygame.VIDEORESIZE:
            screenx = event.w
            screeny = event.h
            screen = pygame.display.set_mode((screenx,screeny),pygame.RESIZABLE)
            screen.fill(color = (255,255,255))
    pygame.display.update()

pygame.quit()
