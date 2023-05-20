import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

width, height = 800, 600

def bresenham(xi,yi,r):
    x = 0
    y = r
    d = 3 - 2*r

    glVertex2f(xi+x, yi + y)


    while(y>=x):
        
        x = x + 1
        if d < 0 :
            d = d + 4*x + 6
        else:
            d = d + 4 * (x-y) + 10
            y = y -1

        glVertex2f(xi+x, yi + y)
        glVertex2f(xi+x, yi-y)
        glVertex2f(xi-x, yi + y)
        glVertex2f(xi-x, yi-y)
        glVertex2f(xi+y, yi + x)
        glVertex2f(xi-y, yi + x)
        glVertex2f(xi-y, yi-x)
        glVertex2f(xi+y, yi-x)
        
        time.sleep(0.00001)


def circleBres():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor(1.0, 1.0, 0.0)

    # llamar la funcion aqui
    bresenham(250,200, 100)
        
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'circle Bresenham')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(circleBres)
    glutIdleFunc(circleBres)
    glutMainLoop()

main()