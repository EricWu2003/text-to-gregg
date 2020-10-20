import math
import pygame
import bezier 
pygame.init()
screen = pygame.display.set_mode((640,480)) #Start the screen

PI = math.pi

class Drawer:
    friction = 0.9
    def __init__(self):
        pass


    def s(self):  #the function to draw the letter s
      # I will probably use a bezier curve to do this


        


    def display(self, screen, connected = False):
        color = pygame.Color(255, 0, 0)

        if not connected:
            for i in range(len(self.points)):
                pygame.draw.ellipse(screen, color, (self.points[i], (1, 1)))
        else:
            pygame.draw.lines(screen, color, False, self.points, 2)

        


drawer = Drawer()
drawer.s()
drawer.display(screen)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #The user closed the window!
            running = False #Stop running

pygame.quit()