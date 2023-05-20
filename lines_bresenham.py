import tkinter as tk
import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0

width, height = 800, 600

def bresenham(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy/float(dx)
    
    x, y = x1, y1 

    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    
    glVertex2f(x, y)
    
    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2*(dy - dx)
        else:
            p = p + 2*dy
 
        x = x + 1 if x < x2 else x - 1


        time.sleep(0.00001)
        glVertex2f(x, y)


def lineBasic():
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
    glutCreateWindow(b'Line Bresenham')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(lineBasic)
    glutIdleFunc(lineBasic)
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
    bresenham(xi,yi,xf,yf)

main()