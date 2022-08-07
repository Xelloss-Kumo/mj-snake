# Snake Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 20
    w = 500

    # on va définir notre créationd 'un objet cube, nous avons donc la position de départ, les directions vers lesquels bouge notre cube et la couleur
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        pass

    # pour dessiner notre cube, on détermine la longueur du coté du carré (dis)
    # on a i qui réprésente la ligne dans laquelle est le cube et j qui est pr la colonne
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Width/Height of each cube
        i = self.pos[0]  # Current row
        j = self.pos[1]  # Current Column

        # pr la method rect ici on va fournir la surface sur laquelle dessiner, la couleur du cube
        # ainsi que la position dans la fenetre ou on veut que ça soit dessiné
        # et enfin le dis-2 (pixel) pour déterminer quelle place colorier
        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        # By multiplying the row and column value of our cube by the width and height of each cube we can determine where to draw it

        # on veut que notre serpent ait des yeux sur sa tete bien entendu, donc si on a en input un eyes=True on va les dessiner
        # pr se faire on part du centre et on dessiner 2 petits cercles dans le cube
        if eyes:  # Draws the eyes
            centre = dis // 2
            radius = 3
            circleMiddle = (i * dis + centre - radius, j * dis + 8)
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos)  # The head will be the front of the snake
        self.body.append(self.head)  # We will add head (which is a cube object)
        # to our body list

        # These will represent the direction our snake is moving
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    # dans notre snake que l'ond essine on veut que pour chaque c (=cube) du body du serpent on dessine le cube associé
    # et si on est en postion 0 donc première position de notre liste de cubes, on est la tête et on a donc les yeux
    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:  # for the first cube in the list we want to draw eyes
                c.draw(surface, True)  # adding the true as an argument will tell us to draw eyes
            else:
                c.draw(surface)  # otherwise we will just draw a cube


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows  # Gives us the distance between the lines

    x = 0  # Keeps track of the current x
    y = 0  # Keeps track of the current y
    for l in range(rows):  # We will draw one vertical and one horizontal line each loop
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
        pygame.draw.line(surface, (255,255,255), (0,y),(w,y))


def redrawWindow(surface):
    # ici on va avoir en plus notre snake à dessiner donc on rajoute notre variable s
    global rows, width, s  # NEW
    surface.fill((0,0,0))
    # on va donc appelé la method draw de notre snake
    s.draw(surface)  # NEW
    drawGrid(width,rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    pass


def message_box(subject, content):
    pass


# Ici rien ne change car on a déjà notre snake s en variable globale qui est maintenant utilisée dans notre redrawWindow
def main():
    global width, rows, s
    width = 500  # Width of our screen
    height = 500  # Height of our screen
    rows = 20  # Amount of rows

    win = pygame.display.set_mode((width, height))  # Creates our screen object

    s = snake((255, 0, 0), (10, 10))  # Creates a snake object which we will code later

    clock = pygame.time.Clock()  # creating a clock object

    flag = True
    # STARTING MAIN LOOP
    while flag:
        pygame.time.delay(50)  # This will delay the game so it doesn't run too quickly
        clock.tick(10)  # Will ensure our game runs at 10 FPS
        redrawWindow(win)  # This will refresh our screen

main()