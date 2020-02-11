##
# Written By Zackery Salzwedel
# This file is unit tests for the CommandWord enumeration
# See project NOTES.txt for more information.
##
import unittest
from CommandWord import CommandWord


class MyTestCase(unittest.TestCase):
    def test_go(self):
        self.assertEqual(CommandWord.GO.value, "go", "Should be go")

    def test_help(self):
        self.assertEqual(CommandWord.HELP.value, "help", "Should be help")

    def test_quit(self):
        self.assertEqual(CommandWord.QUIT.value, "quit", "Should be quit")

    def test_unknown(self):
        self.assertEqual(CommandWord.UNKNOWN.value, "unknown", "Should be unknown")


if __name__ == '__main__':
    unittest.main()
