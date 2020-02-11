##
# Written By Zackery Salzwedel
# This file is unit tests for the functions of the CommandWords collection
# See project NOTES.txt for more information.
##
import unittest
from CommandWord import CommandWord
from CommandWords import CommandWords


class MyTestCase(unittest.TestCase):
    def test_string_words(self):
        commands = CommandWords()
        self.assertEqual(commands.get_string_words(), "go quit help ", "Should be 'go quit help '")

    def test_go(self):
        commands = CommandWords()
        self.assertEqual(commands.get_command_word("go"), CommandWord.GO, "Should be go")

    def test_quit(self):
        commands = CommandWords()
        self.assertEqual(commands.get_command_word("quit"), CommandWord.QUIT, "Should be quit")

    def test_help(self):
        commands = CommandWords()
        self.assertEqual(commands.get_command_word("help"), CommandWord.HELP, "Should be help")

    def test_unknown0(self):
        commands = CommandWords()
        self.assertEqual(commands.get_command_word("unknown"), CommandWord.UNKNOWN, "Should be unknown")

    def test_unknown1(self):
        commands = CommandWords()
        self.assertEqual(commands.get_command_word("1unknown1"), CommandWord.UNKNOWN, "Should be unknown")

    def test_unknown2(self):
        commands = CommandWords()
        self.assertEqual(commands.get_command_word("2unknown2"), CommandWord.UNKNOWN, "Should be unknown")


if __name__ == '__main__':
    unittest.main()
