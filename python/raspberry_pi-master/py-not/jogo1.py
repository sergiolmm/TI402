import pygame as pg


pg.init()
screen = pg.display.set_mode((300,300))

clock = pg.time.Clock()

done = False
is_blue = True
x = 20
y = 20
while not done:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    pressed = pg.key.get_pressed()
    if pressed[pg.K_a]: is_blue = not is_blue    
    if pressed[pg.K_UP]: y -= 3
    if pressed[pg.K_DOWN]: y +=3
    if pressed[pg.K_LEFT]: x -= 3
    if pressed[pg.K_RIGHT]: x +=3


    if is_blue: color = (0,128,255)
    else: color = (255,100,0)

    screen.fill((0,0,0))
    #screen.fill((255,255,255))

    pg.draw.rect(screen, color, pg.Rect(x,y,40,40))

    pg.display.flip()  
    clock.tick(60)      

