import tkinter as tk
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


def linedda():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(1.0, 1.0, 0.0)

    devolverDatos()

    glEnd()
    glutSwapBuffers()

    #root.destroy()

def initial():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(int((glutGet(GLUT_SCREEN_WIDTH)-width)/2),
                       int((glutGet(GLUT_SCREEN_HEIGHT)-height)/2))
    glutCreateWindow(b'Line DDA')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(linedda)
    glutIdleFunc(linedda)
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

    etiqueta4 = tk.Label(root, text="Ingresa la coordenada x del punto final:")
    etiqueta4.pack()
    global entryXf
    entryXf=tk.Entry(root)
    entryXf.pack()

    etiqueta5 = tk.Label(root, text="Ingresa la coordenada y del punto final:")
    etiqueta5.pack()
    global entryYf
    entryYf=tk.Entry(root)
    entryYf.pack()

    botonAceptar=tk.Button(root,text="Aceptar",command=initial)
    botonAceptar.pack()

    root.mainloop()

def devolverDatos():
    xi = int(entryXi.get())
    yi = int(entryYi.get())
    xf = int(entryXf.get())
    yf = int(entryYf.get())
    algoritmo_dda(xi,yi,xf,yf)

main()