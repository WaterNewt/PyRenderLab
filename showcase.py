from pygame.key import ScancodeWrapper
from src.PyRenderLab import *

velocity = 5

class cubeUpdate(Update):
    def __init__(self, object, keys: ScancodeWrapper) -> None:
        if keys[pygame.K_w]:
            object.size+=velocity
        if keys[pygame.K_s]:
            object.size-=velocity
        if keys[pygame.K_d]:
            object.angle_x+=0.01
            object.angle_y+=0.01
            object.angle_z+=0.01
        if keys[pygame.K_a]:
            object.angle_x-=0.01
            object.angle_y-=0.01
            object.angle_z-=0.01

game = Game((100, 100, 100), size=(1000, 800))
objects = []

cube_size = 50
xwidth = 10
ywidth = 10

texture = Texture(color=(0, 255, 0))

for y in range(ywidth):
    for x in range(xwidth):
        new_Cube = Cube(game, cube_size, position=(x*cube_size, y*cube_size), outline_height=1, update=cubeUpdate, texture=texture)
        objects.append(new_Cube)

game.objects(objects)
game.display(30)
