import pygame 

pygame.init()

win = pygame.display.set_mode((600, 600))
on = True
bg = pygame.image.load("j11/hangman/images/bg.jpg")

def stickman():
    pygame.draw.circle(win, (0, 0, 0), (300, 100), 30)
    pygame.draw.line(win, (0, 0, 0), (300, 100), (300, 300), 10)
    pygame.draw.lines(win, (0, 0, 0), False, [(250, 250), (300, 200), (350, 250)], 10)
    pygame.draw.lines(win, (0, 0, 0), False, [(250, 400), (300, 300), (350, 400)], 10)

while on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
    
    win.blit(bg, (0, 0))
    bg = pygame.transform.scale(bg, (600, 600))
    stickman()
    pygame.display.update() 
    