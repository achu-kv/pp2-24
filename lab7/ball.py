import pygame

pygame.init()
done = False
w, h = 500, 500
speed = 20 #px
x, y = w // 2, h // 2 # ball coords.
rad = 25 # radius

clr = (255, 0, 0)
bg = (255, 255, 255)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.draw.circle(screen, clr, (x, y), rad)
screen.fill(bg)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        break
    w, h = screen.get_width(), screen.get_height()
    x0, y0 = x, y

    if pressed[pygame.K_UP]:
        y = y0 - speed
    if pressed[pygame.K_DOWN]:
        y = y0 + speed
    if pressed[pygame.K_LEFT]:
        x = x0 - speed
    if pressed[pygame.K_RIGHT]:
        x = x0 + speed
    
    if rad <= x <= w - rad and rad <= y <= h - rad:
        screen.fill(bg)
        pygame.draw.circle(screen, clr, (x, y), rad)
    else:
        x, y = x0, y0

    pygame.display.update()
    clock.tick(60)



    

    
    
