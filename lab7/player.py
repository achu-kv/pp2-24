import pygame
import os
import random

class Player:
    def __init__(self, path, stage):
        self.stage = stage
        stage.draw_stop()
        self.songs = []
        self.__prev = []
        self.__curr = ''
        files = os.listdir(path)
        for i in files:
            f = i.split('.')
            if f[-1] in ('mp3', 'ogg', 'wav'):
                self.songs.append(os.path.join(path, i))

    def get_current(self):
        return self.__curr
    
    def play(self):
        if self.__curr:
            self.__prev.append(self.__curr)

        toplay = random.choice(self.songs)
        while self.__curr == toplay:
            toplay = random.choice(self.songs)
        self.__curr = toplay
        self.stage.audio_play(self.__curr)
        self.stage.draw_curr(self.__curr)

    def prev(self):
        if not self.__prev:
            return
        toplay = self.__prev.pop()
        self.__curr = toplay
        self.stage.audio_play(self.__curr)
        self.stage.draw_curr(self.__curr)

    def stop(self):
        self.__curr = ''
        self.stage.draw_stop()
        self.stage.audio_stop()

    def state(self):
        if self.__curr:
            return True
        return False

class Stage:
    def __init__(self, x, y):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((x, y))
        self.font = pygame.font.SysFont("comicsansms", 25)

        self.screen.fill((0, 0, 0))
        pygame.display.flip()
    
    def draw_stop(self):
        self.screen.fill((255, 255, 255))
        text = self.font.render('Nothing is playing', True, (0, 0, 0))
        self.screen.blit(text,
        (0, 0))
        pygame.display.flip()
        self.clock.tick(15)

    def draw_curr(self, curr):
        self.screen.fill((255, 255, 255))        
        text = self.font.render(f'{curr}', True, (0, 0, 0))
        self.screen.blit(text,
        (0, 0))
        pygame.display.flip()
    
    def audio_play(self, path):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()

    def audio_stop(self):
        pygame.mixer.music.stop()

pygame.init()
done = False
stage = Stage(500, 500)
# change path if you want...
player = Player("music", stage)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        break

    if pressed[pygame.K_SPACE]:
        if player.state():
            player.stop()
        else:
            player.play()
    elif pressed[pygame.K_LEFT]:
        player.prev()
    elif pressed[pygame.K_RIGHT]:
        player.play()
    player.stage.clock.tick(15)