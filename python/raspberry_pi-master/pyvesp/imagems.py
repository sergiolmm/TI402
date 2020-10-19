import pygame as pg
import os
import time
import thread



image = pg.image.load('./img/Game/L1.png')
if image == None:
    print("erro ao carregar")

image2 = pg.image.load('./img/Game/L2.png')
if image2 == None:
    print("erro ao carregar")


_image_library = {}   # dicionario
def get_image(path):
    global _image_library
    _img = _image_library.get(path)
    if _img == None:
        _img = pg.image.load(path)
        _image_library[path] = _img

    return _img


branco = (255,255,255)
preto  = (0,0,0)

stopThread = False

cor = branco

size = 40 # tamanho do bloco azul
screen_width = 300

pg.init()
screen = pg.display.set_mode((screen_width,300))

clock = pg.time.Clock()

azul_x = 110
azul_y = 10
sentido = 0

def anda_Azul(size,len):
    global azul_x
    global azul_y
    global sentido
    global cor
    global stopThread 
    print("entrou")
    while True:
        if sentido == 0:
            azul_x += 5            
        else:
            azul_x -= 5
        if azul_x <= 0:
            sentido = 0
            cor = branco
        if azul_x >= (len - size):
            sentido = 1 
            cor = preto       
        
        if stopThread:
            break

     #  print(azul_x)
        time.sleep(0.1)



done = False
is_blue = True
x = 40
y = 40
troca = False
print("antes thread")
thread.start_new_thread(anda_Azul,(size,screen_width))



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
    if pressed[pg.K_b]: stopThread = True
    if pressed[pg.K_c]: 
        if stopThread:
            stopThread = False
            thread.start_new_thread(anda_Azul,(size,screen_width))


    if is_blue: color = (0,128,255)
    else: color = (255,100,0)

    #screen.fill((0,0,0))
    screen.fill(cor)

    pg.draw.rect(screen, color, pg.Rect(azul_x,azul_y,size,40))
    if troca:
        troca = not troca
        img = image2
    else:    
        troca = not troca
        img = image
    screen.blit(img, (x,y))

    screen.blit(get_image('./img/Game/L3.png'),(20,80))

   

    pg.display.flip()  
    clock.tick(100)      

