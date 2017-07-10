import unittest

from raspbotics.robot import Robot

class test_robot(unittest.TestCase):
    def test_index(self):
        R = Robot()

        self.assertEqual("robot", R.index())

    def test_see(self):
        return ''
