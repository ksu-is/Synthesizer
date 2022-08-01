import pygame
import note_lists as nl 
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(50)

fps = 60
timer= pygame.time.Clock()
WIDTH = 52 * 35
HEIGHT = 400
screen = pygame.display.set_mode([WIDTH, HEIGHT])
active_whites = []
active_blacks = []

def draw_piano (whites, blacks) :
    white_rects = []
    for i in range(52) :
        rect = pygame.draw.rect(screen, 'white', [i * 35, HEIGHT - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2)
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36) :
        rect = pygame.draw.rect

run = True
while run : 
    timer.tick(fps)
    screen.fill('gray')

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False  

    pygame.display.flip()
pygame.quit()           