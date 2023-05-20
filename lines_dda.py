import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

width, height = 800, 600

def algoritmo_dda(xi,yi,xf,yf):
    dx = abs(xf - xi)
    dy = abs(xf - xi)
    if dx > dy:
        steps = dx
    else:
        steps = dy
    xinc = dx/steps
    yinc = dy/steps

    x = xi
    y = yi
    k = 1
    while k<=steps:

        glVertex2f(round(x), round(y))
        x += xinc
        y += yinc
        k += 1

        time.sleep(0.00001)


def lineDda():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(1.0, 1.0, 0.0)

    algoritmo_dda(50, 50, 350, 350)
        
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'line Dda')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(lineDda)
    glutIdleFunc(lineDda)
    glutMainLoop()

main()