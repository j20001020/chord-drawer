import unittest
from chord_drawer.ChordDrawer import draw_chord

class TestChordDrawer(unittest.TestCase):

    def test_draw_chord_C(self):
        # Test drawing C chord
        frets = [-1, 3, 2, 0, 1, 0]
        # Here we would normally check if the output is as expected,
        # but since draw_chord shows a plot, we will just call it.
        draw_chord("C", frets)

    def test_draw_chord_G(self):
        # Test drawing G chord
        frets = [3, 2, 0, 0, 0, 3]
        draw_chord("G", frets, 3)

    def test_draw_chord_F(self):
        # Test drawing F chord
        frets = [1, 3, 3, 2, 1, 1]
        draw_chord("F", frets)

if __name__ == "__main__":
    unittest.main()