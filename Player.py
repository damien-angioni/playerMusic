#Importations des librairies et des annexes.
import pygame
import pysound
from pygame import mixer
import sys
from Functions import *
#définition des variables
music_list= ["Music/Approaching_Nirvana/Cherry_Blossoms_Approaching_Nirvana.mp3",
            "Music/Jpop/Kimigamitayumenomonogatari.mp3",
            "Music/Metal/Wintersun _Beautiful_Death.mp3",
            "Music/OST/FFBE/Final_Fantasy_Brave_Exvius_Main.mp3",
            "Music/XC_Engage_the_Enemy.mp3"] #Quelques musiques par défaut, utile pour les tests. (Musiques dans des dossiers différents)

def main():
    #Fonction principale du programmende: lecteur de musique.
    print("init")
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption("Frestfeld Music Player")
    pygame.display.set_icon(pygame.image.load("resources/icon.png"))
    screen.fill((25,25,25))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

main() #appel de la fonction principale.