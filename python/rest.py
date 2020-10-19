import pygame as pg
import json
import io
import base64

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

img_url = "https://www.slmm.com.br/ws/exe1/rest_by_id.php?id=67"
img_str = urlopen(img_url).read()
#print(img_str)

data_json = json.loads(img_str)
print(data_json["num"])
img_data = data_json["img_64"]
#print(img_data)
img_file = io.BytesIO(base64.b64decode(str(img_data)))

pg.init()
clock = pg.time.Clock()

white = (255,255,255)
screen = pg.display.set_mode((400,300), pg.RESIZABLE)
screen.fill(white)

image_full = pg.image.load(img_file)
img = pg.transform.scale(image_full,(200,200))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
          pg.quit()
          raise SystemExit

    screen.fill(white)
    screen.blit(img, (10,10))
    pg.display.flip()
    clock.tick(100)





