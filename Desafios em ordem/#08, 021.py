import pygame
pygame.init()
pygame.mixer.music.load('3 palavrinhas mp3.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(15)
