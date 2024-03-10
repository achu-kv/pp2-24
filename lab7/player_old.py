import pygame
import os
import random

class SPlayer:
    def __init__(self, path):
        global screen, font
        self.songs = []
        self.__current = ''
        self.__prev = ''

        files = os.listdir(path)
        for i in files:
            _, ext = i.split('.')
            if ext in ('mp3', 'ogg', 'wav'):
                self.songs.append(os.path.join(path, i))

    def get_current(self):
        return self.__current

    def stop(self, draw=True):
        self.__prev = self.__current
        self.__current = ''
        if draw:
            self.__draw_stop()
        pygame.mixer.music.stop()
        clock.tick(15)

    def play(self):
        toplay = random.choice(self.songs)
        self.__prev = self.__current
        while self.__current == toplay:
            toplay = random.choice(self.songs)
        self.__current = toplay
        self.__draw_curr()
        pygame.mixer.music.load(toplay)
        pygame.mixer.music.play()
        clock.tick(15)
       
    def play_set(self, toplay):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(toplay)
        pygame.mixer.music.play()
        clock.tick(15)    

    def prev(self):
        if not self.__current:
            return
        elif not self.__prev:
            self.play_set(self.__current)
            return
        pygame.mixer.music.load(self.__prev)
        self.__current = self.__prev
        pygame.mixer.music.play()
        self.__draw_curr()
        clock.tick(15)

    def state(self):
        if self.__current:
            return True
        return False

    def __draw_stop(self):
        screen.fill((255, 255, 255))
        pygame.display.flip()
        text = font.render('Nothing is playing', True, (0, 0, 0))
        screen.blit(text,
        (0, 0))
        pygame.display.flip()
        clock.tick(15)

    def __draw_curr(self):
        screen.fill((255, 255, 255))
        pygame.display.flip()
        text = font.render(f'{self.__current}', True, (0, 0, 0))
        screen.blit(text,
        (0, 0))
        pygame.display.flip()


pygame.init()
done = False
pl = SPlayer('music')

global screen, font, clock, x, y

clock = pygame.time.Clock()
x, y = 499, 499
screen = pygame.display.set_mode((x, y))
screen.fill((0, 0, 0))
pygame.display.flip()
font = pygame.font.SysFont("comicsansms", 25)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        break

    if pressed[pygame.K_SPACE]:
        if pl.state():
            pl.stop()
        else:
            pl.play()
    elif pressed[pygame.K_LEFT]:
        pl.prev()
    elif pressed[pygame.K_RIGHT]:
        pl.play()
    clock.tick(15)
    
