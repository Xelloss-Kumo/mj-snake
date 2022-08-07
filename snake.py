# Snake Tutorial Python

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


# Class cube, elle va nous servir à dessiner et manipuler un cube sur le jeu, c'est àd ire un élément du snake, le snack etc
# Cette class possède deux variables locales, le nombre de ligne de notre grille et w la largeur totaleµ
# Nous avons la definition de 3 fonctions
# init pour pouvoir créer un objet cube,
# move pr définir la mouvement d'un cube,
# draw pr dessiner ce cube sur la grille
class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

# Class snake qui va donc représenter notre snake dans le jeu qui sera constitué donc de cubes
# 5 functions
# init pour créer notre objet snake
# move pr le deplacement du snake
# reset pr reste notre snake entre deux parties
# addCube pour rajotuer un cube à notre snake quand il avale la cible
# draw pr dessiner notre snake
class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

# method drawGrid qui nous permettra de dessiner la grille de jeu
# on retrouve nos variables w pour la largeur totale et rows pr le nbre de colonne
# on a aussi une surface qui est le fond de notre grille sur laquelle sera dessiné les colonnes et lignes
def drawGrid(w, rows, surface):
    pass

# method redrawWindow qui va permettre de redessiner la grille de jeu à chaque instant du jeu quand on a un update
def redrawWindow(surface):
    pass

# method qui va permettre de générer ce quie st appelé un snack dans le snake, donc la cible à avaler pr faire grandir le snake
def randomSnack(rows, item):
    pass

# une method qui va nous permettre d'afficher une boite de message pour adresser des infos au joueur (genre you lose)
def message_box(subject, content):
    pass

# la method main, c'est la methode principale de notre code, c'est là que l'orchestration va avoir lieu
def main():
    pass

# cette ligne est juste pr signifier à python que c'est la method main() que l'on veut lancer quand on va jouer notre code
main()