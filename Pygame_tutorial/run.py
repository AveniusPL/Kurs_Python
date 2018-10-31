import pygame, sys
max_tps = 100
pygame.init()  #Inicjalizuje wszystkie moduły.

res = (1280,720)

screen = pygame.display.set_mode(res)

box = pygame.Rect(10,10,50,50)

clock = pygame.time.Clock()
delta = 0.0
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
    # Ticking
    delta += clock.tick() / 1000.0
    while delta > 1/max_tps:
        delta -= 1 / max_tps
    # Checking inputs
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            box.x += 2
        elif keys[pygame.K_s]:
            box.y += 2
        elif keys[pygame.K_a]:
            box.x -= 2
        elif keys[pygame.K_w]:
            box.y -= 2

    # Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 150 , 255), box)
    pygame.display.flip()