import os
import pygame

pygame.init()

def load_chapter(chapter_number):#load in memory a whole chapter
    for page in os.listdir():
        if 'Chapter' in page:
            temp = page.split(" ")
            number = int(temp[1])
            if number == chapter_number:
                chapter.append(pygame.image.load(page).convert())


screen=pygame.display.set_mode((1240,980),pygame.RESIZABLE)
img = pygame.image.load('Chapter 263 page 1.png').convert()
size = img.get_size()
print(size)
input()
y=10
while True:
    screen.blit(img,(0,y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y-=50

pygame.quit()
