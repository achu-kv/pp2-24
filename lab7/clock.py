import pygame
import datetime

def ang_sec():
    n = datetime.datetime.now()
    return 81 - n.second * 6

def ang_min():
    n = datetime.datetime.now()
    return 87 - n.minute * 6

def blitRotateCenter(surf, image, topleft, angle, cl):
    screen.blit(cl, (0, 0))
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)
    pygame.display.flip()
    
    

pygame.init()
done = False

bg = (255, 255, 255)


cl = pygame.image.load('clock.png')
wc, hc = cl.get_rect().width, cl.get_rect().height
scale = wc / hc
mins = pygame.image.load('left-hand.png')
sec = pygame.image.load('right-hand.png')

screen = pygame.display.set_mode((wc, hc))
screen.fill(bg)
screen.blit(cl, (0, 0))

wm, hm = mins.get_rect().width, mins.get_rect().height
ws, hs = sec.get_rect().width, mins.get_rect().height

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        break

    blitRotateCenter(screen, mins, ((wc - wm) // 2, (hc - hm) // 2), ang_min(), cl)
    blitRotateCenter(screen, sec, ((wc - ws) // 2, (hc - hs) // 2 - 20), ang_sec(), cl) 
    
    pygame.display.flip()
    