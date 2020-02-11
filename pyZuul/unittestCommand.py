##
# Written By Zackery Salzwedel
# This file is unit tests for the functions of the Command class
# See project NOTES.txt for more information.
##
import unittest
from CommandWord import CommandWord
from Command import Command


class MyTestCase(unittest.TestCase):
    def test_has_second_word(self):
        command0 = Command("cmd")
        command1 = Command("do", "thing")
        command2 = Command(CommandWord.GO.value, "north")
        command3 = Command(CommandWord.QUIT)
        command4 = Command(CommandWord.HELP)
        self.assertEqual(command0.has_second_word(), False, "Should be false")
        self.assertEqual(command1.has_second_word(), True, "Should be true")
        self.assertEqual(command2.has_second_word(), True, "Should be true")
        self.assertEqual(command3.has_second_word(), False, "Should be false")
        self.assertEqual(command4.has_second_word(), False, "Should be false")

    def test_is_unknown(self):
        command0 = Command("cmd")
        command1 = Command("do", "thing")
        command2 = Command(CommandWord.GO.value, "north")
        command3 = Command(CommandWord.QUIT)
        command4 = Command(CommandWord.HELP)
        self.assertEqual(command0.is_unknown(), True, "Should be true")
        self.assertEqual(command1.is_unknown(), True, "Should be true")
        self.assertEqual(command2.is_unknown(), False, "Should be false")
        self.assertEqual(command3.is_unknown(), False, "Should be false")
        self.assertEqual(command4.is_unknown(), False, "Should be false")

    def test_get_command_word(self):
        command0 = Command("cmd")
        command1 = Command("do", "thing")
        command2 = Command(CommandWord.GO.value, "north")
        command3 = Command(CommandWord.QUIT)
        command4 = Command(CommandWord.HELP)
        self.assertEqual(command0.get_command_word(), CommandWord.UNKNOWN, "Should be unknown")
        self.assertEqual(command1.get_command_word(), CommandWord.UNKNOWN, "Should be unknown")
        self.assertEqual(command2.get_command_word(), CommandWord.GO, "Should be go")
        self.assertEqual(command3.get_command_word(), CommandWord.QUIT, "Should be quit")
        self.assertEqual(command4.get_command_word(), CommandWord.HELP, "Should be help")

    def test_get_second_word(self):
        command0 = Command("cmd")
        command1 = Command("do", "thing")
        command2 = Command(CommandWord.GO.value, "north")
        command3 = Command(CommandWord.QUIT)
        command4 = Command(CommandWord.HELP)
        self.assertEqual(command0.get_second_word(), None, "Should be None")
        self.assertEqual(command1.get_second_word(), "thing", "Should be thing")
        self.assertEqual(command2.get_second_word(), "north", "Should be north")
        self.assertEqual(command3.get_second_word(), None, "Should be None")
        self.assertEqual(command4.get_second_word(), None, "Should be None")


if __name__ == '__main__':
    unittest.main()
