#Importations des librairies et des annexes.
from pygame import mixer
from tkinter import *
import random
import tkinter.font as font
from tkinter import filedialog
from Functions import *
#définition des variables


def main():
    #Fonction principale du programmen de: lecteur de musique.
    fenetre=Tk()
    fenetre.title("Scarlet Music Player")
    fenetre.geometry("1080x720")
    fenetre.iconbitmap("resources/icon.ico")
    #initialize mixer
    #mixer.init()
    fenetre.mainloop()

main() #appel de la fonction principale.