##
# Written By Zackery Salzwedel
# This file is unit tests for the functions of the Scenario class
# See project NOTES.txt for more information.
##
import unittest
from Room import Room
from Scenario import Scenario


class MyTestCase(unittest.TestCase):
    def test_basic_info(self):
        self.assertEqual(Scenario.name(), "default")
        self.assertEqual(Scenario.info(), "World Map")

    def test_all_exits(self):
        curr = Scenario.load()

        self.assertEqual(curr.get_description(), "North America")

        direction = "south"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "South America")

        direction = "south"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Antarctica")

        direction = "northwest"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "South America")

        direction = "north"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "North America")

        direction = "east"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Europe")

        direction = "south"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Africa")

        direction = "south"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Antarctica")

        direction = "north"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Africa")

        direction = "north"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Europe")

        direction = "east"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Asia")

        direction = "south"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Australia")

        direction = "south"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Antarctica")

        direction = "northeast"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Australia")

        direction = "north"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Asia")

        direction = "east"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "North America")

        direction = "west"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Asia")

        direction = "west"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Europe")

        direction = "west"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "North America")

        direction = "south"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "South America")

        direction = "east"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Africa")

        direction = "east"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Australia")

        direction = "east"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "South America")

        direction = "west"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Australia")

        direction = "west"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "Africa")

        direction = "west"
        curr = curr.get_exit(direction)
        self.assertEqual(curr.get_description(), "South America")


if __name__ == '__main__':
    unittest.main()
