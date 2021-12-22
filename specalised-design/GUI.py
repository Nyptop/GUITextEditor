import pygame

from Text import Text

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode([500, 500])

text = Text()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                text.insert('q')
            if event.key == pygame.K_w:
                text.insert('w')
            if event.key == pygame.K_DELETE:
                text.delete()
            if event.key == pygame.K_BACKSPACE:
                text.backspace()
            if event.key == pygame.K_LEFT:
                text.cursor_left()
            if event.key == pygame.K_RIGHT:
                text.cursor_right()

    screen.fill((255, 255, 255))

    for line_number, line in enumerate(text.get_text()):
        textsurface = myfont.render(line, False, (0, 0, 0))
        screen.blit(textsurface,(0,line_number*20))

    pygame.display.flip()

pygame.quit()