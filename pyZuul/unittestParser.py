##
# Written By Zackery Salzwedel
# This file is unit tests for the functions of the Parser class
# See project NOTES.txt for more information.
##
from CommandWord import CommandWord
from Parser import Parser
import unittest


class MyTestCase(unittest.TestCase):
    def test_string_commands(self):
        self.assertEqual(Parser.string_commands(), "go quit help ", "Should be 'go quit help '")

    def test_get_command(self):
        self.assertEqual(Parser.parse_command("get help").get_command_word(), CommandWord.UNKNOWN, "Should be unknown")
        self.assertEqual(Parser.parse_command("do thing").get_command_word(), CommandWord.UNKNOWN, "Should be unknown")
        self.assertEqual(Parser.parse_command("unknown").get_command_word(), CommandWord.UNKNOWN, "Should be unknown")
        self.assertEqual(Parser.parse_command("go north").get_command_word(), CommandWord.GO, "Should be unknown")
        self.assertEqual(Parser.parse_command("quit").get_command_word(), CommandWord.QUIT, "Should be quit")
        self.assertEqual(Parser.parse_command("help").get_command_word(), CommandWord.HELP, "Should be help")


if __name__ == '__main__':
    unittest.main()
