import pygame
from pygame.locals import*

from OpenGL.GL import*
from OpenGL.GLU import*

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

def draw():
    glBegin(GL_LINES)
    for e in arestas:
        for vertex in e:
            glVertex3iv(vertices[vertex])
    glEnd()

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Exemplo")

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0, 0, 0-5)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    draw()
    pygame.display.flip()
    pygame.time.wait(15)
