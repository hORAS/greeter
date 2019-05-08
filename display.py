#!/usr/bin/env python
"""
Description: Binary string animation. Could be used in screensavers, et al.
Usage: python display.py
       Strike "Esc" to exit the program.
       You can pass the class constructor a dictionary of config values:
           BinaryAnimation({'resolution': (800, 600), 'bin_len': 8, 
                            'delay_ms': 3000, 'background_color': (0, 0, 90)})
Note: This program requires the Pygame library from www.pygame.org.
"""
#try:
import sys
import re
from random import choice
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEMOTION, QUIT, FULLSCREEN
#except ImportError, err:
#    print (sys.stderr, "Couldn't load module. %s" % (err))
#    sys.exit(2)

class PygText(object):
    def __init__(self, surface):
        self.surface = surface

    def show(self, msg, font_size=12, pos='center', 
             font_color=(255, 255, 255)):
        """
        Write text on a surface.
        By default, the text is positioned fully centered.
        Position values: bottom, bottomleft, bottomright, center, left, 
                         midbottom, midleft, midright, midtop, right, top, 
                         topleft, topright.
        You can also supply a tuple of x/y coordinates.
        """
        #font = pygame.font.Font(None, font_size)
        font = pygame.font.Font('./fonts/roboto/Roboto-Regular.ttf', 48)
        ren = font.render(msg, 1, font_color) # render font with transparent background
        ren_rect = ren.get_rect()

        # Position the text:
        if isinstance(pos, tuple):  
            # Position anywhere:
            ren_rect = ren.get_rect()
            ren_rect[0] = pos[0]
            ren_rect[1] = pos[1]
        else:
            # Set a named position attribute:        
            setattr(ren_rect, pos, getattr(self.surface.get_rect(), pos))

        # Display the text:
        self.surface.blit(ren, ren_rect)
        pygame.display.update(ren_rect)

    def clear(self, color=(0, 0, 0)):
        """Clear the surface."""
        self.surface.fill(color)
        pygame.display.update()

class displayMessage(object):
    def __init__(self, config={}):
        """Initialize the screen and data."""
        # Default configuration values:
        self.config = {'resolution': (600, 400), 'bin_len': 32, 
                       'delay_ms': 1000, 'background_color': (0, 0, 0)}
        # Update any user supplied configuration values:
        self.config.update(config)
        # Apply the configuration values:
        self.resolution = self.config['resolution']
        self.delay_ms = self.config['delay_ms']
        self.bin_len = self.config['bin_len']  # Amount of bits to display.
        # RGB value of the background color:
        self.background_color = self.config['background_color']  

        # Initialize pygame:
        pygame.init() 
        pygame.font.init()
        pygame.display.set_caption('Binary Animation')

        # Create a screen surface to draw on:
        self.screen = pygame.display.set_mode(self.resolution, FULLSCREEN)

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Generate a string of bits, separated every "half-octect":
        self.bits = 'Hola'#''.join(['1010 ' for x in range(self.bin_len / 4)])

    def _shuffle(self):
        """Shuffle the message."""
        # Randomize only the bits, not the spaces:
        self.bits = re.sub('\d', lambda ignored: choice('10'), self.bits)

    def _delay(self):
        """Delay animation iterations."""
        pygame.time.wait(self.delay_ms) 

    def displayText(self, msg):
        t = PygText(self.screen)
        t.clear(self.background_color)
        t.show(msg, 25, 'center', (0, 255, 0))

    def mainLoop(self):
        """Begin the animation."""
        t = PygText(self.screen)

        #motion = 0

        # Begin the main loop of the program:
        while True:
            for event in pygame.event.get():
                # require a certain amount of motion to stop the screensaver
                #if event.type == MOUSEMOTION:
                    #motion = motion + 1

                if event.type == QUIT or (event.type == KEYDOWN):
                    pygame.quit()
                    return

            # Example of displaying the binary number animations:
            
            #t.clear(self.background_color)  # Erase text before overwriting.
            
            #t.show(self.bits, 15, 'topright', (105, 105, 105))
            #t.show(self.bits, 15, 'topleft', (105, 105, 105))
            #self._shuffle()
            #t.show(self.bits, 25, 'center', (0, 255, 0))
            #self._shuffle()
            #t.show(self.bits, 15, 'bottomleft', (105, 105, 105))
            #t.show(self.bits, 15, 'bottomright', (105, 105, 105))

            #self._shuffle()
            #self._delay()

#if __name__ == '__main__':
#animation = displayMessage({'delay_ms': 1100, 'background_color': (0, 0, 0)})
#animation.mainLoop()


#def blit_text(surface, text, pos, font, color=pygame.Color('white')):
#    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
#    space = font.size(' ')[0]  # The width of a space.
#    max_width, max_height = surface.get_size()
#    x, y = pos
#    for line in words:
#        for word in line:
#            word_surface = font.render(word, 0, color)
#            word_width, word_height = word_surface.get_size()
#            if x + word_width >= max_width:
#                x = pos[0]  # Reset the x.
#                y += word_height  # Start on new row.
#            surface.blit(word_surface, (x, y))
#            x += word_width + space
#        x = pos[0]  # Reset the x.
#        y += word_height  # Start on new row.