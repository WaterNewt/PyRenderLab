# PyRenderLab
A very simple, yet robust, 3D framework made in PyGame.

**WARNING: THIS IS JUST A PERSONAL PROJECT, NOT FOR COMMERCIAL USE**
---

## Setup
- Installing libraries:
`pip3 install -r requirements.txt`
- Run the setup file:
`python3 setup.py install`

## Use
Here is a sample script utilizing this framework
```python
from pyrenderlab import *
from typing import Final

# Constants
WINDOW_SIZE: Final[tuple] = (800, 600)
VELOCITY: Final[int] = 5
PLAYER_SIZE: Final[int] = 125
FPS: Final[int] = 30


# Update Function
def update(keys):
    if keys[K_w]:
        player.y -= VELOCITY
    if keys[K_s]:
        player.y += VELOCITY
    if keys[K_a]:
        player.x -= VELOCITY
    if keys[K_d]:
        player.x += VELOCITY
    if keys[K_ESCAPE] or keys[K_q]:
        game.stop()
    player.angle_x += 0.05
    player.angle_y += 0.05
    player.angle_z += 0.05


# Initialize game
game = Game(bg_color=(100, 100, 100), size=WINDOW_SIZE, update=update)

# Create Player cube
playerTexture = Texture(color=(0, 0, 255))
player = Cube(game, PLAYER_SIZE, texture=playerTexture, position=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2, 0))
print(player)

# Add player to the game
game.add_objects([player])

# Display game at specific FPS
game.display(FPS)
```

## License
This project is licensed under the MIT license. Learn more [here](LICENSE)