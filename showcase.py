import src.PyRenderLab as pyrenderlab

VELOCITY = 5


def update():
    keys = game.keys
    if keys[pyrenderlab.K_w]:
        new_shape.y -= VELOCITY
    if keys[pyrenderlab.K_s]:
        new_shape.y += VELOCITY
    if keys[pyrenderlab.K_a]:
        new_shape.x -= VELOCITY
    if keys[pyrenderlab.K_d]:
        new_shape.x += VELOCITY
    if keys[pyrenderlab.K_q]:
        game.stop()
    diff_x = (game.mousex - centerx) / 500
    diff_y = (game.mousey - centery) / 500
    new_shape.angle_y = diff_x
    new_shape.angle_x = diff_y


game = pyrenderlab.Game(bg_color=(0, 0, 0), update=update, icon_image=".github/images/icon.png")
centerx, centery = game.width / 2, game.height / 2

new_shape = pyrenderlab.Cube(game, 150)

all_shapes = [new_shape]
game.add_objects(all_shapes)

game.display(60)
