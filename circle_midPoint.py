import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

width, height = 800, 600

def midPoint(xi,yi,r):

    x = 0
    y = r
    d = 1 - r

    glVertex2f(xi+x, yi + y)


    while(y > x):
        
        x = x + 1
        if d <= 0 :
            d = d + 2*x + 1
        else:
            y = y - 1
            d = d + 2*x - 2*y + 1
        
        glVertex2f(xi+x, yi + y)
        glVertex2f(xi+x, yi-y)
        glVertex2f(xi-x, yi + y)
        glVertex2f(xi-x, yi-y)
        glVertex2f(xi+y, yi + x)
        glVertex2f(xi-y, yi + x)
        glVertex2f(xi-y, yi-x)
        glVertex2f(xi+y, yi-x)
        
        time.sleep(0.00001)

def circleMidP():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor(1.0, 1.0, 0.0)

    midPoint(250,200, 100)
        
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'circle midPoint')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(circleMidP)
    glutIdleFunc(circleMidP)
    glutMainLoop()

main()
