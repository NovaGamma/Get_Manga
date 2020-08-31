import os
import pygame

pygame.init()

def load_chapter(chapter_number):#load in memory a whole chapter
    chapter = []
    for page in os.listdir():
        if 'Chapter' in page:
            temp = page.split(" ")
            number = int(temp[1])
            if number == chapter_number:
                img = pygame.image.load(page).convert()
                if len(chapter) > 0:
                    chapter.append([img,chapter[-1][0].get_height()+chapter[-1][1],img])
                else:
                    chapter.append([img,0,img])
    return chapter

screenx = 1240
screeny = 980

screen=pygame.display.set_mode((screenx,screeny),pygame.RESIZABLE)
img = pygame.image.load('Chapter 263 page 1.png').convert()
size = img.get_size()
y=10
scroll_y = 0
scalling = 5
chapter_number = 263
chapter = load_chapter(chapter_number)
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
