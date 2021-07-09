import pygame

class Musica:
    def __init__(self):
        pass

    def ini_music():
        pygame.init() 
        pygame.mixer.init()

    def musica_ini(self):
        pygame.init()
        pygame.mixer.music.load('./Projeto_Final/ini.wav') 
        pygame.mixer.music.play()
        #pygame.event.wait()

    def musica_win(self):
        pygame.init()
        pygame.mixer.music.load('./Projeto_Final/winner.wav') 
        pygame.mixer.music.play()
        #pygame.event.wait()

    def musica_gameover(self):
        pygame.init()
        pygame.mixer.music.load('./Projeto_Final/final.wav') 
        pygame.mixer.music.play()
        #pygame.event.wait()  

    def digitar(self):
        pygame.init()
        pygame.mixer.music.load('./Projeto_Final/digitando.mp3')
        pygame.mixer.music.play() 