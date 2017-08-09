import random
import pygame
import math
#create a visual triangle within a triangle

width = 400
height = 300
pygame.init()
 
#Reminding myself the colors
#black = [  0,  0,  0]
#white = [255,255,255]
#blue =  [  0,  0,255]
#green = [  0,255,  0]
#red =   [255,  0,  0]

w = width
h = height
 
screen = pygame.display.set_mode((w,h))



x = w/2
y = h/2

cornerA = (0, h) 

cornerB = (w/2, 0)

cornerC = (w,h)

  

for dots in range(100000):
   (cornerWidth) = random.randrange(0,w+1,w/2)
    
   if cornerWidth == 0:
       (cornerHeight) = h
   elif cornerWidth == (w/2):
       (cornerHeight)= h*0
   elif cornerWidth == (w):
        (cornerHeight) = h
        
        
   x = (cornerWidth + x)/2
   y = (cornerHeight + y)/2
   red = (1-(x)/(w))*255 
   blue = ((x)/(w))*255
   green =(1-(y)/(h))*255
   color = (red,green,blue)
   
   pygame.draw.line(screen, color, (x,y),(x,y),1)
   pygame.display.update()
    
pygame.display.flip()
pygame.display.quit()
pygame.quit()
  



