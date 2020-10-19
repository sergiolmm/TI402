import pygame as pg 
import time
import thread

image = pg.image.load('./img/L1.png')
if image == None:
    print("Erro ao carregar")
    quit()

image1 = pg.image.load('./img/L2.png')
if image1 == None:
    print("Erro ao carregar")
    quit()
image2 = pg.image.load('./img/L3.png')
if image2 == None:
    print("Erro ao carregar")
    quit()


# criar funcao que sera executada na thread
i_x = 10
i_y = 60
sentido2 = 0
img = image

def anda_img(size, len):
    global i_x
    global i_y
    global sentido2
    global img
    anda = True
    while True:
        if sentido2 == 0:
            i_x += 5
        else:
            i_x -= 5

        if i_x <= 0:
            sentido2 = 0
        if anda:    
            img = image1
        else:
            img = image2
        if i_x >= (len - size):
            sentido2 = 1
            

        anda = not anda


        time.sleep(0.05)

branco = (255,255,255)
preto = (0,0,0)
cor = branco

a_x = 10
a_y = 10
sentido = 0  # 0 esquerda 1 direita

def anda_azul(size, len):
    global a_x
    global a_y
    global sentido
    global cor

    while True:
        if sentido == 0:
            a_x += 5
        else:
            a_x -= 5

        if a_x <= 0:
            sentido = 0
            cor = preto

        if a_x >= (len - size):
            sentido = 1
            cor = branco

        time.sleep(0.08)




screen_width = 300

pg.init()
screen = pg.display.set_mode((screen_width, 300))

clock = pg.time.Clock()
done = False
is_blue = True
color = (0,0,0)
x = y = 0
thread.start_new_thread(anda_azul, (40, screen_width))
thread.start_new_thread(anda_img, (40, screen_width))

#pg.mixer.music.load('./img/music.mp3')
#pg.mixer.music.play(0)

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

    if is_blue: 
        color = (0,128,255)
    else: 
        color = (255,100,0)

    screen.fill(cor)

    pg.draw.rect(screen, color, pg.Rect(a_x,a_y,40,40))

    screen.blit(img,(i_x,i_y))



    pg.display.flip()  
    clock.tick(100)   