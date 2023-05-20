import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

width, height = 800, 600

def algoritmo_basico_de_lineas(xi,yi,xf,yf):
    m = round((yf-yi)/(xf-xi))
    auxy = yi
    auxx = xi
    while auxy <= yf:
        #print("basico","x:",auxx,"y:",auxy)
        glVertex2f(auxx, auxy)
        auxx += 1
        auxy += m
        time.sleep(0.00001)

def lineBasic():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(1.0, 1.0, 0.0)

    algoritmo_basico_de_lineas(50, 50, 350, 350)
        
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'line Basic')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(lineBasic)
    glutIdleFunc(lineBasic)
    glutMainLoop()

main()