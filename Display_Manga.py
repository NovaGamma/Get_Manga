import pygame

pygame.init()

screen=pygame.display.set_mode((1240,980),pygame.RESIZABLE)
img = pygame.image.load('Chapter 263 page 1.png').convert()
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
