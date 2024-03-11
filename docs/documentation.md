# Documentation for PyRenderLab

## Constants
- All the constants are located in src/PyRenderLab/constants.py
- Most of the constants were taken from PyGame.
- The file also contains the error raise messages, which are used in the raise tests for raise assertion.

Here are some examples:
```python
# The "a" key
pyrenderlab.K_a

# Used to control angle in Shape3D.rotate()
pyrenderlab.ANGLE_X
pyrenderlab.ANGLE_Y
pyrenderlab.ANGLE_Z

# Error raise message for when the outline_height argument in Shape3D is not an integer
pyrenderlab.INVALID_OUTLINE_HEIGHT_TYPE
```

## `pyrenderlab.Game()`
The main class of the game

### Attributes
- `bg_color`: This is the color that will be filled as the background of the window. This is usually a tuple, but can be a `Union[pygame.Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]`
- `update`: This is a function (usually named `update`), that will run every tick of the game. The tick of the game is controlled by the `fps` argument of `Game.display()`
- `size`: The size of the window of the game. Usually a tuple with two items (width and height)
- `window_title`: The title of the window.
- `icon_image`: The icon of the window. On a MacOS device, this icon will be displayed on the dock.

### Methods
- `add_objects`: Add objects to the game. The `instances` of any class that is a subclass of the class `Shape3D`. Will raise a TypeError with message `pyrenderlab.INVALID_OBJECT_TYPE`, if any of the items in the array are not a subclass of the Shape3D class.
- `display`: Simply displays the window of the game. The `fps` must be an integer. This will determine the tick of the loop of the game.
- `stop`: Stops the game by stopping the loop. Usually used inside of an update function.

## `pyrenderlab.Shape3D`
This is an abstract class for all 3D geometrical shapes. This class must only be used for creating new 3D shapes.

### Attributes
All attributes here are same for other child classes of this class.
- `gameInstance`: The instance of the Game class. This is used for getting information on the window of the game. This can be found in the `draw` method for the 3D shape classes.
- `size`: A float which determines the size of the shape.
- `texture`: An instance of the `Texture` class, for the physical apperance of the shape.
- `position`: The position of the center of the shape on the window screen. This must be a 3-Dimensional array.
- `angle_x`, `angle_y` and `angle_z`: These are 3 attributes that control the angle of the shape across the 3 dimensions.

### Methods
Methods of all the Shape3D subclasses. These are obviously not all the methods, these are just methods that will may useful to the developer.
- `rotate`: This is a method that may or may not be deprecated in the future. This is because it is much better to simply use the angle attributes of the class.
- `draw`: An abstract method for drawing the 3D shape. This method is automatically ran in the `display` method of the `Game` class.
Checkout the code itself for perhaps more methods.

## Subclasses of Shape3D
These are all classes that inherit from the `Shape3D` abstract class. These are all the usable 3 dimensional shapes. The attributes and the methods of these classes are the same as the attributes and the methods of the `Shape3D` class.

### `pyrenderlab.Cube()`
A cube is a solid object with six equal square faces, twelve straight edges, and eight vertices where the edges meet.

### `pyrenderlab.Cube()`
A 3D prism is a solid shape with two identical polygonal bases connected by parallelogram faces.

## `pyrenderlab.Texture()`
**Coming Soon...**