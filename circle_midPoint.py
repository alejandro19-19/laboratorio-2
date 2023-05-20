import tkinter as tk
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

    devolverDatos()

    glEnd()
    glutSwapBuffers()

    #root.destroy()

def initial():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(int(width/2),int(height/2))
    glutInitWindowPosition(int((glutGet(GLUT_SCREEN_WIDTH)-width)/2),
                       int((glutGet(GLUT_SCREEN_HEIGHT)-height)/2))
    glutCreateWindow(b'Circle MidPoint')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(circleMidP)
    glutIdleFunc(circleMidP)
    glutMainLoop()

def main():
   
    root = tk.Tk()
    root.geometry("300x230")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    root.title("Algoritmo de búsqueda")


    etiqueta2 = tk.Label(root, text="Ingresa la coordenada x del punto inicial:")
    etiqueta2.pack()
    global entryXi
    entryXi=tk.Entry(root)
    entryXi.pack()

    etiqueta3 = tk.Label(root, text="Ingresa la coordenada y del punto inicial:")
    etiqueta3.pack()
    global entryYi
    entryYi=tk.Entry(root)
    entryYi.pack()

    etiqueta4 = tk.Label(root, text="Ingresa el radio de la circunferencia:")
    etiqueta4.pack()
    global entryR
    entryR=tk.Entry(root)
    entryR.pack()

    botonAceptar=tk.Button(root,text="Aceptar",command=initial)
    botonAceptar.pack()

    root.mainloop()

def devolverDatos():
    xi = int(entryXi.get())
    yi = int(entryYi.get())
    r = int(entryR.get())
    midPoint(xi,yi,r)

main()