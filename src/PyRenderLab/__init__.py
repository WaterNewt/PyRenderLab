import sys
import pygame
import numpy as np
from os import PathLike
from abc import ABC, abstractmethod
from src.PyRenderLab.constants import *
from typing import Iterable, Union, Tuple, Sequence, IO

RGBAOutput = Tuple[int, int, int, int]
Position = Tuple[float, float, float]
ColorValue = Union[pygame.Color, int, str, Tuple[int, int, int], RGBAOutput, Sequence[int]]
Coordinate = Union[Tuple[float, float], Sequence[float], pygame.math.Vector2]
Number = Union[float, int]


def inform(message: str, exit_code=-1):
    print(message)
    sys.exit(exit_code)


class Shape3D(ABC):
    """
    An Abstract Base Class for a 3D geometrical shape in a game.
    """
    def __init__(self, gameInstance: 'Game', size: Number, texture: 'Texture' = None, position: Position = None, outline_height: int = 1) -> None:
        """Initialization of the shape.

        Args:
            gameInstance (Game): The instance of the Game class.
            size (float): The size of the shape.
            texture (Texture): The Texture of the shape. Must be a Texture class.
            position (Iterable): The position of the shape on the screen.
        """
        if not isinstance(outline_height, int):
            inform("Outline must be integer.")
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.line_height = outline_height
        self.game = gameInstance
        self.size = size
        self.texture = (255, 255, 255) if texture is None else texture
        self.position = [gameInstance.screen.get_width()/2, gameInstance.screen.get_height()/2] if position is None else position
        self.x, self.y, self.z = self.position
        self.rotation_x = np.array([])
        self.rotation_y = np.array([])
        self.rotation_z = np.array([])
        self.rotated_vertices = None
        self.projected_vertices = None

    def calculations(self):
        self.rotation_x = np.array([[1, 0, 0],
                               [0, np.cos(self.angle_x), -np.sin(self.angle_x)],
                               [0, np.sin(self.angle_x), np.cos(self.angle_x)]])

        self.rotation_y = np.array([[np.cos(self.angle_y), 0, np.sin(self.angle_y)],
                               [0, 1, 0],
                               [-np.sin(self.angle_y), 0, np.cos(self.angle_y)]])

        self.rotation_z = np.array([[np.cos(self.angle_z), -np.sin(self.angle_z), 0],
                               [np.sin(self.angle_z), np.cos(self.angle_z), 0],
                               [0, 0, 1]])

        self.rotated_vertices = np.dot(self.vertices, self.rotation_x)
        self.rotated_vertices = np.dot(self.rotated_vertices, self.rotation_y)
        self.rotated_vertices = np.dot(self.rotated_vertices, self.rotation_z)

        self.projected_vertices = self.rotated_vertices[:, :2] + (self.x, self.y)

    def rotate(self, angle: int, value: Number):
        if angle == ANGLE_X:
            self.angle_x = value
        elif angle == ANGLE_Y:
            self.angle_y = value
        elif angle == ANGLE_Z:
            self.angle_z = value
        else:
            raise ValueError("Please use either ANGLE_X, ANGLE_Y or ANGLE_Z")

    @abstractmethod
    def draw(self):
        """
        An Abstract Method for drawing the 3D shape.
        """
        pass


class Game:
    def __init__(self, bg_color: ColorValue = None, update=None, size: Tuple[float, float] = (800, 600), window_title: str = None, icon_image: Union[str, bytes, PathLike[str], PathLike[bytes], IO[bytes], IO[str]] = None) -> None:
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(size)
        if window_title is not None:
            self.caption = window_title
            pygame.display.set_caption(self.caption)
        if icon_image is not None:
            icon = pygame.image.load(icon_image)
            pygame.display.set_icon(icon)
        self.update = None if update is None else update
        self.bg_color = (0, 0, 0) if bg_color is None else bg_color
        self.object_instances = []
        self.run = True

    def add_objects(self, instances: list):
        self.object_instances = instances

    def display(self, fps: int):
        clock = pygame.time.Clock()

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
            self.screen.fill(self.bg_color)
            try:
                for i in self.object_instances:
                    i.draw()
            except AttributeError:
                pass
            if self.update is not None:
                self.update(keys=pygame.key.get_pressed())
            pygame.display.update()
            clock.tick(fps)

    def stop(self):
        self.run = False

    def __repr__(self) -> str:
        return f'Game(update={None if self.update is None else str(self.update.__name__)})'


class Texture:
    def __init__(self, img_path: str = None, color: ColorValue = None) -> None:
        self.img_path = img_path
        self.color = color

    def __repr__(self) -> str:
        return f'Texture(img_path={str(self.img_path)}, color={str(tuple(self.color))})'


class Cube(Shape3D):
    def __init__(self, gameInstance: Game, size: float, texture: Texture = None, position: Iterable = None, outline_height=1) -> None:
        super().__init__(gameInstance, size, texture, position, outline_height)
        self.edges = [
            (0, 1), (1, 3), (3, 2), (2, 0),
            (4, 5), (5, 7), (7, 6), (6, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.vertices = np.array([])

    def draw(self):
        self.vertices = np.array([[x, y, z] for x in ((self.size+self.z)/2, -(self.size+self.z)/2) for y in ((self.size+self.z)/2, -(self.size+self.z)/2) for z in ((self.size+self.z)/2, -(self.size+self.z)/2)])
        super().calculations()
        faces = [
            [self.projected_vertices[i] for i in face] for face in [(0, 1, 3, 2), (4, 5, 7, 6), (0, 4, 6, 2), (1, 5, 7, 3), (0, 1, 5, 4), (2, 3, 7, 6)]
        ]

        for face in faces:
            if isinstance(self.texture, Iterable):
                pygame.draw.polygon(self.game.screen, ColorValue(self.texture), face)
            else:
                if self.texture.img_path:
                    image = pygame.image.load(self.texture.img_path)
                    rect = image.get_rect()
                    rect.center = np.mean(face, axis=0)
                    self.game.screen.blit(image, rect.topleft)
                elif self.texture.color:
                    pygame.draw.polygon(self.game.screen, self.texture.color, face)

        for edge in self.edges:
            start = self.projected_vertices[edge[0]]
            end = self.projected_vertices[edge[1]]
            pygame.draw.line(self.game.screen, (0, 0, 0), start, end, self.line_height)

    def __repr__(self) -> str:
        return f'Cube(game=({self.game}), size={str(self.size)}, position={str(list(self.position))})'


class Triangle(Shape3D):
    def __init__(self, gameInstance: Game, size: float, texture: Texture = None, position: Iterable = None, outline_height=1) -> None:
        super().__init__(gameInstance, size, texture, position, outline_height)
        self.edges = [
            (0, 1), (1, 2), (2, 0),
            (3, 4), (4, 5), (5, 3),
            (0, 3), (1, 4), (2, 5),
        ]
        self.velocity = 0.05
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

    def draw(self):
        self.vertices = np.array([
            [-(self.size+self.z)/2, -(self.size+self.z)/3, -(self.size+self.z)/2],
            [(self.size+self.z)/2, -(self.size+self.z)/3, -(self.size+self.z)/2],
            [0, (self.size+self.z)/3, -(self.size+self.z)/2],
            [-(self.size+self.z)/2, -(self.size+self.z)/3, (self.size+self.z)/2],
            [(self.size+self.z)/2, -(self.size+self.z)/3, (self.size+self.z)/2],
            [0, (self.size+self.z)/3, (self.size+self.z)/2]
        ])
        super().calculations()
        faces = [
            [self.projected_vertices[i] for i in face] for face in [
                (0, 1, 2),
                (3, 4, 5),
                (0, 1, 4, 3),
                (1, 2, 5, 4),
                (0, 2, 5, 3)
            ]
        ]

        for face in faces:
            if isinstance(self.texture, Iterable):
                pygame.draw.polygon(self.game.screen, ColorValue(self.texture), face)
            else:
                if self.texture.img_path:
                    image = pygame.image.load(self.texture.img_path)
                    rect = image.get_rect()
                    rect.center = np.mean(face, axis=0)
                    self.game.screen.blit(image, rect.topleft)
                elif self.texture.color:
                    pygame.draw.polygon(self.game.screen, self.texture.color, face)

        for edge in self.edges:
            start = self.projected_vertices[edge[0]]
            end = self.projected_vertices[edge[1]]
            pygame.draw.line(self.game.screen, (0, 0, 0), start, end, self.line_height)

    def __repr__(self) -> str:
        return f'Triangle(game=({self.game}), size={str(self.size)}, position={str(list(self.position))})'
