import pygame
#import OpenGL

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

superfice = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

normals = (
    (0, 0, -1),
    (-1, 0, 0),
    (0, 0, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, -1, 0)
)

cores = (
    (0, 0, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 1),
    (0, 0, 1)
)

arestas = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def cubo():
    glBegin(GL_LINES)
    for edge in arestas:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == event.K_LEFT:
                    glTranslatef(-0.5, 0, 0)

                if event.key == event.K_RIGHT:
                    glTranslatef(0.5, 0, 0)

                if event.key == event.K_UP:
                    glTranslatef(0, 1, 0)

                if event.key == event.K_DOWN:
                    glTranslatef(0, -1, 0)


                if event.key == pygame.K_s:
                    glRotatef(5, 5, 0, 0)

                if event.key == pygame.K_w:
                    glRotatef(-5, 5, 0, 0)

                if event.key == pygame.K_d:
                    glRotatef(-5, 0, -5, 0)

                if event.key == pygame.K_a:
                    glRotatef(5, 0, -5, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)

                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cubo()
        pygame.display.flip()
        pygame.time.wait(10)
main()
