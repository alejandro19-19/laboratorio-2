import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def algoritmo_basico_de_lineas(xini,yini,xfin,yfin):
    m = round((yfin-yini)/(xfin-xini))
    auxy = yini
    auxx = xini
    glBegin(GL_LINES)
    while auxy <= yfin:
        glVertex2f(auxx, auxy)
        auxx += 1
        auxy += m
    glEnd()

def algoritmo_dda(xini,yini,xfin,yfin):
    dx = abs(xfin - xini)
    dy = abs(yfin - yini)
    if dx > dy:
        steps = dx
    else:
        steps = dy
    xinc = dx/steps
    yinc = dy/steps

    x = xini
    y = yini
    k = 1
    glBegin(GL_LINES)
    while k<=steps:
        glVertex2f(round(x), round(y))
        x += xinc
        y += yinc
        k += 1
    glEnd()

def main():
    pygame.init()
    display = (1000, 1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    
    glTranslatef(-5.0,0.0, -20)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    glColor3f(1.0, 0.0, 0.0)
    
    algoritmo_basico_de_lineas(0,0,4,4)
    
    glColor3f(0.0, 1.0, 0.0)
    
    algoritmo_dda(2,2,5,5)

if __name__ == '__main__':
    main()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        display()
        
        pygame.display.flip()