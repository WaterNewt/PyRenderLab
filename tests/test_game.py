import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import src.PyRenderLab as pyrenderlab


class TestRaises(unittest.TestCase):
    def setUp(self):
        self.game = pyrenderlab.Game()

    def test_objects_raise(self):
        with self.assertRaisesRegex(TypeError, pyrenderlab.INVALID_OBJECT_TYPE):
            self.game.add_objects([69])

    def test_update_arg_raise(self):
        def update():
            pass
        with self.assertRaises(ValueError):
            self.new_game = pyrenderlab.Game(update=update)

    def test_update_type_raise(self):
        with self.assertRaisesRegex(TypeError, pyrenderlab.INVALID_UPDATE_TYPE):
            self.new_game = pyrenderlab.Game(update=69)


if __name__ == '__main__':
    unittest.main()
