import pygame
from pygame.draw import *


def draw_bamboo_sticks():
    rect(screen, green, (500, 400, 35, 120))

    rect(screen, green, (500, 245, 35, 140))

    stick1 = pygame.Surface((28, 90))
    stick1.fill(green)
    stick1.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick1, -20), (495, 140))

    stick2 = pygame.Surface((15, 120))
    stick2.fill(green)
    stick2.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick2, -20), (520, 10))

    rect(screen, green, (350, 450, 10, 100))

    rect(screen, green, (350, 340, 10, 100))

    stick3 = pygame.Surface((8, 80))
    stick3.fill(green)
    stick3.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick3, -10), (350, 250))

    stick4 = pygame.Surface((6, 70))
    stick4.fill(green)
    stick4.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick4, -13), (360, 175))

    rect(screen, green, (110, 450, 14, 70))

    rect(screen, green, (110, 365, 14, 75))

    stick5 = pygame.Surface((10, 50))
    stick5.fill(green)
    stick5.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick5, -13), (110, 300))

    stick6 = pygame.Surface((6, 70))
    stick6.fill(green)
    stick6.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick6, -13), (120, 220))

    rect(screen, green, (900, 400, 15, 110))

    rect(screen, green, (900, 260, 15, 130))

    stick7 = pygame.Surface((10, 70))
    stick7.fill(green)
    stick7.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick7, -13), (900, 180))

    stick8 = pygame.Surface((6, 100))
    stick8.fill(green)
    stick8.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(stick8, -13), (915, 70))


def draw_bamboo_branches():
    branch1 = pygame.Surface((380, 250))
    branch1.fill(peach)
    branch1.set_colorkey(peach)
    pygame.draw.arc(branch1, green, (0, 0, 380, 250), 2.7, 4, 2)
    screen.blit(pygame.transform.rotate(branch1, -80), (510, 170))

    pygame.draw.arc(screen, green, (560, 20, 600, 300), 1.7, 2.9, 2)

    pygame.draw.arc(screen, green, (-100, 70, 600, 400), 0.4, 1.5, 2)

    branch2 = pygame.Surface((800, 400))
    branch2.fill(peach)
    branch2.set_colorkey(peach)
    pygame.draw.arc(branch2, green, (0, 0, 800, 400), -0.5, 0.25, 2)
    screen.blit(pygame.transform.rotate(branch2, 80), (70, 200))

    branch3 = pygame.Surface((250, 100))
    branch3.fill(peach)
    branch3.set_colorkey(peach)
    pygame.draw.arc(branch3, green, (0, 0, 250, 100), -1, 0.4, 2)
    screen.blit(pygame.transform.rotate(branch3, 85), (235, 330))

    pygame.draw.arc(screen, green, (160, 210, 200, 300), 0.5, 1.5, 2)

    branch4 = pygame.Surface((250, 70))
    branch4.fill(peach)
    branch4.set_colorkey(peach)
    pygame.draw.arc(branch4, green, (0, 0, 250, 70), -0.5, 1, 2)
    screen.blit(pygame.transform.rotate(branch4, 95), (355, 300))

    branch5 = pygame.Surface((500, 300))
    branch5.fill(peach)
    branch5.set_colorkey(peach)
    pygame.draw.arc(branch5, green, (0, 0, 500, 300), 0.05, 0.9, 2)
    screen.blit(pygame.transform.rotate(branch5, 105), (310, 135))

    branch6 = pygame.Surface((400, 150))
    branch6.fill(peach)
    branch6.set_colorkey(peach)
    pygame.draw.arc(branch6, green, (0, 0, 400, 150), -0.2, 0.7, 2)
    screen.blit(pygame.transform.rotate(branch6, 95), (95, 320))

    branch7 = pygame.Surface((500, 300))
    branch7.fill(peach)
    branch7.set_colorkey(peach)
    pygame.draw.arc(branch7, green, (0, 0, 500, 300), -0.1, 0.7, 2)
    screen.blit(pygame.transform.rotate(branch7, 100), (70, 200))

    branch8 = pygame.Surface((500, 150))
    branch8.fill(peach)
    branch8.set_colorkey(peach)
    pygame.draw.arc(branch8, green, (0, 0, 500, 150), -0.7, 0.2, 2)
    screen.blit(pygame.transform.rotate(branch8, 95), (-20, 345))

    branch9 = pygame.Surface((500, 400))
    branch9.fill(peach)
    branch9.set_colorkey(peach)
    pygame.draw.arc(branch9, green, (0, 0, 500, 400), -0.7, -0.1, 2)
    screen.blit(pygame.transform.rotate(branch9, 85), (-255, 237))

    branch10 = pygame.Surface((500, 120))
    branch10.fill(peach)
    branch10.set_colorkey(peach)
    pygame.draw.arc(branch10, green, (0, 0, 500, 120), -0.4, 0.8, 2)
    screen.blit(pygame.transform.rotate(branch10, 95), (895, 210))

    branch11 = pygame.Surface((500, 150))
    branch11.fill(peach)
    branch11.set_colorkey(peach)
    pygame.draw.arc(branch11, green, (0, 0, 500, 150), -0.8, 0.3, 2)
    screen.blit(pygame.transform.rotate(branch11, 85), (730, 250))

    branch11 = pygame.Surface((500, 300))
    branch11.fill(peach)
    branch11.set_colorkey(peach)
    pygame.draw.arc(branch11, green, (0, 0, 500, 300), -0.1, 0.8, 2)
    screen.blit(pygame.transform.rotate(branch11, 110), (865, 22))

    branch12 = pygame.Surface((500, 400))
    branch12.fill(peach)
    branch12.set_colorkey(peach)
    pygame.draw.arc(branch12, green, (0, 0, 500, 400), -0.7, 0.1, 2)
    screen.blit(pygame.transform.rotate(branch12, 65), (415, 30))


def draw_leaves():
    leaf1 = pygame.Surface((70, 12))
    leaf1.fill(peach)
    leaf1.set_colorkey(peach)
    pygame.draw.ellipse(leaf1, green, (0, 0, 70, 12))
    screen.blit(pygame.transform.rotate(leaf1, -70), (670, 53))
    screen.blit(pygame.transform.rotate(leaf1, -70), (710, 47))
    screen.blit(pygame.transform.rotate(leaf1, -70), (730, 40))
    screen.blit(pygame.transform.rotate(leaf1, -70), (750, 33))
    screen.blit(pygame.transform.rotate(leaf1, -70), (770, 30))
    screen.blit(pygame.transform.rotate(leaf1, -70), (600, 205))
    screen.blit(pygame.transform.rotate(leaf1, -70), (630, 190))
    screen.blit(pygame.transform.rotate(leaf1, -70), (660, 190))

    leaf2 = pygame.Surface((70, 13))
    leaf2.fill(peach)
    leaf2.set_colorkey(peach)
    pygame.draw.ellipse(leaf2, green, (0, 0, 70, 13))
    screen.blit(pygame.transform.rotate(leaf2, 70), (385, 235))
    screen.blit(pygame.transform.rotate(leaf2, 70), (360, 227))
    screen.blit(pygame.transform.rotate(leaf2, 70), (410, 247))
    screen.blit(pygame.transform.rotate(leaf2, 70), (230, 75))
    screen.blit(pygame.transform.rotate(leaf2, 70), (250, 77))
    screen.blit(pygame.transform.rotate(leaf2, 70), (270, 87))
    screen.blit(pygame.transform.rotate(leaf2, 70), (290, 94))
    screen.blit(pygame.transform.rotate(leaf2, 70), (330, 105))

    leaf3 = pygame.Surface((50, 7))
    leaf3.fill(peach)
    leaf3.set_colorkey(peach)
    pygame.draw.ellipse(leaf3, green, (0, 0, 50, 7))
    screen.blit(pygame.transform.rotate(leaf3, 80), (313, 348))
    screen.blit(pygame.transform.rotate(leaf3, 80), (303, 338))
    screen.blit(pygame.transform.rotate(leaf3, 80), (290, 333))
    screen.blit(pygame.transform.rotate(leaf3, 80), (305, 233))
    screen.blit(pygame.transform.rotate(leaf3, 80), (290, 230))
    screen.blit(pygame.transform.rotate(leaf3, 80), (282, 223))
    screen.blit(pygame.transform.rotate(leaf3, 80), (274, 213))
    screen.blit(pygame.transform.rotate(leaf3, 80), (266, 213))
    screen.blit(pygame.transform.rotate(leaf3, -80), (377, 307))
    screen.blit(pygame.transform.rotate(leaf3, -80), (385, 303))
    screen.blit(pygame.transform.rotate(leaf3, -80), (395, 301))
    screen.blit(pygame.transform.rotate(leaf3, -80), (407, 200))
    screen.blit(pygame.transform.rotate(leaf3, -80), (416, 198))
    screen.blit(pygame.transform.rotate(leaf3, -80), (423, 190))
    screen.blit(pygame.transform.rotate(leaf3, -80), (430, 182))
    screen.blit(pygame.transform.rotate(leaf3, -80), (437, 178))

    leaf4 = pygame.Surface((40, 7))
    leaf4.fill(peach)
    leaf4.set_colorkey(peach)
    pygame.draw.ellipse(leaf4, green, (0, 0, 40, 7))
    screen.blit(pygame.transform.rotate(leaf4, 80), (70, 366))
    screen.blit(pygame.transform.rotate(leaf4, 80), (58, 355))
    screen.blit(pygame.transform.rotate(leaf4, 80), (45, 352))
    screen.blit(pygame.transform.rotate(leaf4, 80), (50, 280))
    screen.blit(pygame.transform.rotate(leaf4, 80), (37, 272))
    screen.blit(pygame.transform.rotate(leaf4, 80), (28, 270))
    screen.blit(pygame.transform.rotate(leaf4, 80), (20, 265))
    screen.blit(pygame.transform.rotate(leaf4, 80), (12, 262))
    screen.blit(pygame.transform.rotate(leaf4, -80), (150, 333))
    screen.blit(pygame.transform.rotate(leaf4, -80), (162, 328))
    screen.blit(pygame.transform.rotate(leaf4, -80), (172, 325))
    screen.blit(pygame.transform.rotate(leaf4, -80), (170, 250))
    screen.blit(pygame.transform.rotate(leaf4, -80), (185, 245))
    screen.blit(pygame.transform.rotate(leaf4, -80), (193, 238))
    screen.blit(pygame.transform.rotate(leaf4, -80), (201, 231))
    screen.blit(pygame.transform.rotate(leaf4, -80), (211, 228))

    leaf5 = pygame.Surface((60, 7))
    leaf5.fill(peach)
    leaf5.set_colorkey(peach)
    pygame.draw.ellipse(leaf5, green, (0, 0, 60, 7))
    screen.blit(pygame.transform.rotate(leaf5, 80), (825, 255))
    screen.blit(pygame.transform.rotate(leaf5, 80), (838, 258))
    screen.blit(pygame.transform.rotate(leaf5, 80), (853, 267))
    screen.blit(pygame.transform.rotate(leaf5, 80), (800, 118))
    screen.blit(pygame.transform.rotate(leaf5, 80), (810, 120))
    screen.blit(pygame.transform.rotate(leaf5, 80), (820, 133))
    screen.blit(pygame.transform.rotate(leaf5, 80), (830, 146))
    screen.blit(pygame.transform.rotate(leaf5, 80), (845, 150))
    screen.blit(pygame.transform.rotate(leaf5, -80), (970, 100))
    screen.blit(pygame.transform.rotate(leaf5, -80), (985, 90))
    screen.blit(pygame.transform.rotate(leaf5, -80), (992, 82))
    screen.blit(pygame.transform.rotate(leaf5, -80), (1000, 74))
    screen.blit(pygame.transform.rotate(leaf5, -80), (1008, 70))
    screen.blit(pygame.transform.rotate(leaf5, -80), (938, 222))
    screen.blit(pygame.transform.rotate(leaf5, -80), (952, 215))
    screen.blit(pygame.transform.rotate(leaf5, -80), (965, 215))


def draw_panda():
    pygame.draw.ellipse(screen, white, (600, 370, 200, 130))
    pygame.draw.ellipse(screen, black, (580, 420, 50, 150))

    paw1 = pygame.Surface((54, 75))
    paw1.fill(black)
    paw1.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw1, 10), (595, 433))

    paw2 = pygame.Surface((40, 80))
    paw2.fill(black)
    paw2.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw2, -20), (597, 491))

    pygame.draw.rect(screen, black, (675, 370, 60, 150))

    paw3 = pygame.Surface((48, 75))
    paw3.fill(black)
    paw3.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw3, -15), (660, 497))

    paw4 = pygame.Surface((100, 60))
    paw4.fill(peach)
    paw4.set_colorkey(peach)
    pygame.draw.ellipse(paw4, black, (0, 0, 100, 60))
    screen.blit(pygame.transform.rotate(paw4, 30), (630, 520))

    pygame.draw.polygon(screen, black, [(730, 500), (700, 520), (730, 550), (730, 500)])

    paw5 = pygame.Surface((150, 70))
    paw5.fill(peach)
    paw5.set_colorkey(peach)
    pygame.draw.ellipse(paw5, black, (0, 0, 150, 70))
    screen.blit(pygame.transform.rotate(paw5, 60), (690, 450))

    face1 = pygame.Surface((170, 100))
    face1.fill(peach)
    face1.set_colorkey(peach)
    pygame.draw.ellipse(face1, white, (0, 0, 170, 100))
    screen.blit(pygame.transform.rotate(face1, 80), (570, 300))

    face2 = pygame.Surface((170, 80))
    face2.fill(peach)
    face2.set_colorkey(peach)
    pygame.draw.ellipse(face2, white, (0, 0, 170, 80))
    screen.blit(pygame.transform.rotate(face1, -60), (590, 290))

    face3 = pygame.Surface((150, 80))
    face3.fill(peach)
    face3.set_colorkey(peach)
    pygame.draw.ellipse(face3, white, (0, 0, 170, 80))
    screen.blit(pygame.transform.rotate(face3, 10), (582, 385))

    ear1 = pygame.Surface((90, 45))
    ear1.fill(peach)
    ear1.set_colorkey(peach)
    pygame.draw.ellipse(ear1, black, (0, 0, 80, 40))
    screen.blit(pygame.transform.rotate(ear1, 55), (557, 300))

    ear2 = pygame.Surface((80, 45))
    ear2.fill(peach)
    ear2.set_colorkey(peach)
    pygame.draw.ellipse(ear2, black, (0, 0, 80, 40))
    screen.blit(pygame.transform.rotate(ear2, -65), (662, 312))

    pygame.draw.ellipse(screen, black, (595, 455, 40, 25))

    pygame.draw.ellipse(screen, black, (580, 400, 30, 45))

    pygame.draw.ellipse(screen, black, (630, 410, 40, 40))

    pygame.draw.rect(screen, black, (720, 375, 15, 90))


def draw_panda_child():
    pygame.draw.ellipse(screen, white, (460, 550, 100, 65))

    paw1 = pygame.Surface((35, 70))
    paw1.fill(peach)
    paw1.set_colorkey(peach)
    pygame.draw.ellipse(paw1, black, (0, 0, 40, 70))
    screen.blit(pygame.transform.rotate(paw1, -50), (465, 575))

    paw2 = pygame.Surface((20, 40))
    paw2.fill(black)
    paw2.set_colorkey(peach)
    screen.blit(pygame.transform.rotate(paw2, -20), (443, 580))

    paw3 = pygame.Surface((30, 20))
    paw3.fill(peach)
    paw3.set_colorkey(peach)
    pygame.draw.ellipse(paw3, black, (0, 0, 30, 20))
    screen.blit(pygame.transform.rotate(paw3, -50), (440, 605))

    paw4 = pygame.Surface((50, 40))
    paw4.fill(peach)
    paw4.set_colorkey(peach)
    pygame.draw.ellipse(paw4, black, (0, -10, 50, 40))
    screen.blit(pygame.transform.rotate(paw4, 60), (525, 580))

    face1 = pygame.Surface((85, 50))
    face1.fill(peach)
    face1.set_colorkey(peach)
    pygame.draw.ellipse(face1, white, (0, 0, 85, 50))
    screen.blit(pygame.transform.rotate(face1, 80), (450, 518))

    face2 = pygame.Surface((85, 40))
    face2.fill(peach)
    face2.set_colorkey(peach)
    pygame.draw.ellipse(face2, white, (0, 0, 85, 40))
    screen.blit(pygame.transform.rotate(face1, -60), (455, 512))

    face3 = pygame.Surface((75, 40))
    face3.fill(peach)
    face3.set_colorkey(peach)
    pygame.draw.ellipse(face3, white, (0, 0, 75, 40))
    screen.blit(pygame.transform.rotate(face3, 10), (455, 560))

    ear1 = pygame.Surface((45, 22))
    ear1.fill(peach)
    ear1.set_colorkey(peach)
    pygame.draw.ellipse(ear1, black, (0, 0, 40, 20))
    screen.blit(pygame.transform.rotate(ear1, 55), (445, 512))

    ear2 = pygame.Surface((40, 22))
    ear2.fill(peach)
    ear2.set_colorkey(peach)
    pygame.draw.ellipse(ear2, black, (0, 0, 40, 20))
    screen.blit(pygame.transform.rotate(ear2, -65), (490, 520))

    pygame.draw.ellipse(screen, black, (462, 590, 20, 15))

    pygame.draw.ellipse(screen, black, (455, 560, 15, 22))

    pygame.draw.ellipse(screen, black, (480, 565, 20, 20))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1050, 700))

black = (0, 0, 0)
peach = (255, 175, 128)
green = (0, 104, 55)
white = (255, 255, 255)

screen.fill(peach)

draw_bamboo_sticks()
draw_bamboo_branches()
draw_leaves()
draw_panda()
draw_panda_child()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()