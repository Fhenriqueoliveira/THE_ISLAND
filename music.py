import pygame

class Musica:
    def __init__(self):
        pass

    def ini_music():
        pygame.init() 
        pygame.mixer.init()

    def musica_ini(self):
        pygame.mixer.music.load('ini.wav') 
        pygame.mixer.music.play()
        #pygame.event.wait()


    def musica_win(self):
        pygame.mixer.music.load('winner.wav') 
        pygame.mixer.music.play()
        #pygame.event.wait()
    def musica_gameover(self):
        pygame.mixer.music.load('final.wav') 
        pygame.mixer.music.play()
        #pygame.event.wait()  