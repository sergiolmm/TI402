import pygame
import time
import thread
import io 

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

img_url = "https://www.slmm.com.br/ws/exe1/foto_by_id.php?id=67"
img_str = urlopen(img_url).read()

img_file = io.BytesIO(img_str)

img_full = pygame.image.load(img_file)

img = pygame.transform.scale(img_full, (150,150))

image = pygame.image.load('./img/L2E.png')
if image == None:
    print("Erro ao carregar imagem")

pos_x = 0
pos_x2 = 350
sentido = 0  # 0 esqueda 1 direita

def andar(size, tamanho):
    global pos_x
    global pos_x2
    global sentido
    global is_blue

    while True:
        if sentido == 0:
            pos_x += 5
            pos_x2 -= 7
        else:
            pos_x -= 5
            pos_x2 += 7

        if pos_x <= 0:
            sentido = 0
            is_blue = True


        if pos_x >= (tamanho-size):
            sentido = 1
            is_blue = False
        
        time.sleep(0.1)    



pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

thread.start_new_thread(andar,(60,400))

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]: is_blue = not is_blue
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))

        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)

        pygame.draw.rect(screen, color, pygame.Rect(pos_x, y, 60, 60))

        screen.blit(image,(pos_x2,80))
        
        screen.blit(img,(pos_x2,150))

        pygame.display.flip()
        clock.tick(60)