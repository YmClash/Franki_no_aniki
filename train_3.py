import pygame
import datetime
import time

date = datetime.datetime

largeur = 500
hauteur = 500
pygame.init()
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("YMC")

screen.fill((250, 201, 0))

rect = pygame.Rect(100, 100, 300, 50)
cara = pygame.Rect(100,50,150,25)
pygame.draw.rect(screen, (255, 0, 0), rect)
pygame.draw.rect(screen,(225,0,0),cara)



clock = pygame.time.Clock()
while True :

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()

    pygame.display.update()

# ##
#
#
#     screen.fill((0, 0, 0, 0))
#     pygame.draw.circle(screen,(0,0,0),(250,250),100,0)
#     pygame.draw.rect(screen, (255, 100, 0), rect)
#     pygame.display.update()
#     time.sleep(5)
#
#
# print(date)
