##
# Written By Zackery Salzwedel
# This file is unit tests for the functions of the Parser class
# See project NOTES.txt for more information.
##
import unittest
from Room import Room


class MyTestCase(unittest.TestCase):
    def test_description(self):
        batcave = Room("The Batcave")
        manor = Room("Wayne Manor")
        grounds = Room("Manor Grounds")
        self.assertEqual(batcave.get_description(), "The Batcave")
        self.assertEqual(manor.get_description(), "Wayne Manor")
        self.assertEqual(grounds.get_description(), "Manor Grounds")

    def test_description_verbose(self):
        batcave = Room("The Batcave")
        manor = Room("Wayne Manor")
        grounds = Room("Manor Grounds")
        batcave.set_exit("up", manor)
        batcave.set_exit("out", grounds)
        manor.set_exit("down", batcave)
        manor.set_exit("out", grounds)
        grounds.set_exit("in", manor)
        self.assertEqual(batcave.get_description_verbose(), "Thing: The Batcave Paths: up out ")
        self.assertEqual(manor.get_description_verbose(), "Thing: Wayne Manor Paths: down out ")
        self.assertEqual(grounds.get_description_verbose(), "Thing: Manor Grounds Paths: in ")

    def test_exits(self):
        batcave = Room("The Batcave")
        manor = Room("Wayne Manor")
        grounds = Room("Manor Grounds")
        batcave.set_exit("up", manor)
        batcave.set_exit("out", grounds)
        manor.set_exit("down", batcave)
        manor.set_exit("out", grounds)
        grounds.set_exit("in", manor)
        self.assertEqual(batcave.get_exit("up").get_description(), "Wayne Manor")
        self.assertEqual(batcave.get_exit("out").get_description(), "Manor Grounds")
        self.assertEqual(manor.get_exit("down").get_description(), "The Batcave")
        self.assertEqual(manor.get_exit("out").get_description(), "Manor Grounds")
        self.assertEqual(grounds.get_exit("in").get_description(), "Wayne Manor")
        self.assertEqual(grounds.get_exit("down"), None)


if __name__ == '__main__':
    unittest.main()
