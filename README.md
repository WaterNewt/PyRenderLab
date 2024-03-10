# PyRenderLab
A very simple, 3D framework made in PyGame. Just a personal project of mine.

---

## Setup
- Installing libraries:
`pip3 install -r requirements.txt`
- Run the setup file:
`python3 setup.py install`

## Important notes
- The `img_path` attribute of the Texture class is functional but still in its infancy. This is due to its recent development.
- This project is not made for commercial use. This is just a personal project of my mine.
- All the 3D shapes in the library, are just classes inherited from the `Shape3D` abstract class. So feel free to add your own 3D shapes and contribute!

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
game = Game(bg_color=(100, 100, 100), size=WINDOW_SIZE, update=update, window_title="Showcase", icon_image="./.github/images/icon.png")

# Create Player cube
playerTexture = Texture(color=(0, 0, 255))
player = Cube(game, PLAYER_SIZE, texture=playerTexture, position=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2, 0))
print(player)

# Add player to the game
game.add_objects([player])

# Display game at specific FPS
game.display(FPS)
```
And this is what the window would look like:
### Window:
<img src="./.github/images/screenshot0.png" width=500>

### Window Icon:
<img src="./.github/images/icon.png" width=100>

### Functionality:
- Spin in the x, y and z axes
- Move with *w*, *a*, *s* and *d*

## License
This project is licensed under the MIT license. Learn more [here](LICENSE)