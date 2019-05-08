import sys
#
import pygame as pg
from pygame.locals import K_ESCAPE, QUIT, FULLSCREEN,KEYDOWN



pg.init()
clock = pg.time.Clock()

print(pg.QUIT)
#screenSettings
screen = pg.display.set_mode((800, 800))
pg.display.set_caption('Greeter')
screen_rect = screen.get_rect()
# set up the colors
#BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
#RED = (255, 0, 0)
#GREEN = (0, 255, 0)
#BLUE = (0, 0, 255)
# set up fonts

font = pg.font.Font('./fonts/roboto/Roboto-Regular.ttf', 48)
rendered_text = font.render("YAHAAA \n soy too", True, pg.Color("dodgerblue"))
text_rect = rendered_text.get_rect(midleft=(900, screen_rect.centery))   

done = False
while not done:
    for event in pg.event.get():
        print(event.type )
        if event.type == QUIT or event.type == K_ESCAPE or event.type == KEYDOWN:
            done = True
            #return

        #if event.type == QUIT or (event.type == KEYDOWN)or (event.type == K_ESCAPE):
            #pygame.quit()
            #return
            
    if text_rect.centerx > screen_rect.centerx:
        #print (text_rect.centerx)
        text_rect.move_ip(-5, 0)        
    
    screen.fill(pg.Color("gray5"))
    screen.blit(rendered_text, text_rect)
    
    pg.display.update()
    clock.tick(60)
    
pg.quit()
sys.exit()

