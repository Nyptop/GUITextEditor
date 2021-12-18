import pygame

from Text import Text

pygame.init()

screen = pygame.display.set_mode([500, 500])

text = Text()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                text.add_char('q')
            if event.key == pygame.K_DELETE:
                text.delete()

    # listen for key strokes, ready to update the text class

    screen.fill((255, 255, 255))

    # draw text based on the text class

    pygame.display.flip()

pygame.quit()