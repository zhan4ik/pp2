import pygame
from math import sqrt
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))
    clock = pygame.time.Clock()
    #Starting and ending positions of pen
    prevX = 0
    prevY = 0 
    #Starting and ending positions of rectangle while drawing:
    prevX1 = -1
    prevY1 = -1
    currentX1 = -1
    currentY1 = -1

    color = (255,255,255)
    screen.fill((0, 0, 0))
    isMouseDown = False
    while True:      
        pressed = pygame.key.get_pressed()
        #Current x and y
        currentX = prevX
        currentY = prevY       
        for event in pygame.event.get():#pen
            if event.type == pygame.QUIT:#exiting the program
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #right
                    isMouseDown = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: #left
                    isMouseDown = False
            if event.type == pygame.MOUSEMOTION:#pen
                #if the mouse has moved, add a point to the list for the handle
                currentX =  event.pos[0]
                currentY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONDOWN: #rectangle
                #if the mouse has moved, add a point to the list for the rectangle
                if event.button == 1: 
                    isMouseDown = True
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]    
                    prevX1 =  event.pos[0]
                    prevY1 =  event.pos[1]
            #if isMouseDown is false, then we can end our drawing
            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))
            #if isMouseDown is true, then we can draw shapes
            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]
        #color
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_r: 
                    color = (255, 0, 0) 
                elif event.key == pygame.K_g: 
                    color = (0, 255, 0) 
                elif event.key == pygame.K_b: 
                    color = (0, 0, 255) 
                elif event.key == pygame.K_w: 
                    color = (255,255,255)  
        if isMouseDown:#pen
            pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

        if pressed[pygame.K_1]: #rectangle
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color,pygame.Rect(r), 1)

        if pressed[pygame.K_2]:     #circle 
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1: 
                screen.blit(baseLayer, (0, 0))
                c = centerCirc(prevX1, prevY1, currentX1, currentY1) 
                ra = radiusCirc(prevX1, prevY1, currentX1, currentY1) 
                pygame.draw.circle(screen, color, c, ra, 1)
        if pressed[pygame.K_3]: #eraser
            if isMouseDown:
                pygame.draw.line(screen, (0,0,0), (prevX, prevY), (currentX, currentY),30)

        prevX = currentX
        prevY = currentY
        
        pygame.display.flip()
        clock.tick(60)
def calculateRect(x1, y1, x2, y2):
#Top left x coordinate, Top left y coordinate, Bottom right x coordinate, Bottom right y coordinate
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
#finding the center of the rectangle
def centerCirc(x1, y1, x2, y2): 
    return abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2)
#finding the radius of the circle
def radiusCirc(x1, y1, x2, y2): 
    return sqrt((((abs(x1 - x2) / 2) ** 2) + (abs(y1 - y2) / 2) ** 2))
main()