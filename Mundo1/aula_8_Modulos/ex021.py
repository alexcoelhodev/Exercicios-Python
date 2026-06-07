#Faca um programa em python que abra e reproduza um audio de arquivo

import subprocess

subprocess.run(["afplay", "ex021.mp3"])

input("Pressione ENTER para sair...")

'''import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("ex021.mp3")   # ou "ex021.ogg"
pygame.mixer.music.play()'''