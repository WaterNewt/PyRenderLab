import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import src.PyRenderLab as pyrenderlab


class TestPrism(unittest.TestCase):
    def setUp(self):
        self.game = pyrenderlab.Game()
        self.new_shape = pyrenderlab.Prism(self.game, 100)
        self.new_shape.rotate(pyrenderlab.ANGLE_X, 69)
        self.game.add_objects([self.new_shape])

    def test_add(self):
        self.assertTrue(self.new_shape in self.game.object_instances)

    def test_rotate(self):
        self.assertEquals(self.new_shape.angle_x, 69)


class TestCube(unittest.TestCase):
    def setUp(self):
        self.game = pyrenderlab.Game()
        self.new_shape = pyrenderlab.Cube(self.game, 100)
        self.new_shape.rotate(pyrenderlab.ANGLE_X, 69)
        self.game.add_objects([self.new_shape])

    def test_add(self):
        self.assertTrue(self.new_shape in self.game.object_instances)

    def test_rotate(self):
        self.assertEquals(self.new_shape.angle_x, 69)


class TestRaises(unittest.TestCase):
    def setUp(self):
        self.game = pyrenderlab.Game()

    def test_outline_height_cube(self):
        with self.assertRaisesRegex(ValueError, pyrenderlab.INVALID_OUTLINE_HEIGHT_TYPE):
            self.game.add_objects([pyrenderlab.Cube(self.game, 100, outline_height=0.69)])

    def test_outline_height_prism(self):
        with self.assertRaisesRegex(ValueError, pyrenderlab.INVALID_OUTLINE_HEIGHT_TYPE):
            self.game.add_objects([pyrenderlab.Prism(self.game, 100, outline_height=0.69)])


if __name__ == "__main__":
    unittest.main()
