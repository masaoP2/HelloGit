#-*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

#gittest
def main():
    (w, h) = (300,200) #window size
    (x, y) = (10, h//2) # racket senter
    (bx, by) = (w//2, h//2)
    vx, vy = 8, 5


    pygame.init()
    pygame.display.set_mode((w, h))
    screen = pygame.display.get_surface()

    pygame.mixer.init(frequency = 44100) # initial setting
    
    while(1):
        pygame.display.update() #update display
        pygame.time.wait(30) # interval of updating
        screen.fill ((0, 0, 0, 0)) # fill screen with black
        
        #racket
        pygame.draw.line(screen, (255, 255 ,255), (x, y-20),(x, y+20), 10)

        #ball
        pygame.draw.line(screen, (255, 0, 0),(bx-3, by),(bx+3, by),8)

        pressed_key = pygame.key.get_pressed()

        # racket movement
        if pressed_key[K_UP]:
            y -= 10
        
        if pressed_key[K_DOWN]:
            y += 10
        
        # racket inside window
        if y < 20:
            y = 20
        if y > h-20:
            y = h-20

        # ball movement
        bx += vx
        by += vy

        # ball inside window
        if ( bx > w and vx > 0):
            vx = -vx
        
        if (0 > by and vy < 0) or (by > h and vy > 0):
            vy = -vy
        
        #raxcket hit
        if (y-30 < by < y+30 and vx < 0 and 7 < bx < 15):
            vx = -vx
        
        # ball went outside
        if bx  < -50:
            pygame.time.weit(1000)
            bx, by - (w//2, h//2)
            theta = 2*math.pi*random.random()
            vx = int(math.cos(theta) * 7) + 2*math.cos(theta)/abs(math.cos(theta))
            vy = int(math.sin(theta) * 7) + 2*math.sin(theta)/abs(math.sin(theta))

        for event in pygame.event.get():
            #close button pushed
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #escape key pushed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    main()
