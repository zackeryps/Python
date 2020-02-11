##
# Written By Zackery Salzwedel
# This file is unit tests for the functions of the Game class
# See project NOTES.txt for more information.
##
import unittest
from Game import Game


class MyTestCase(unittest.TestCase):
    def test_msg_scenario_list(self):
        expected = ""
        expected += "\nScenarios: "
        expected += "\ndefault: World Map"
        expected += "\nfamily: Simpson's Family Tree"
        self.assertEqual(Game.msg_scenario_list(), expected)

    def test_msg_welcome(self):
        expected = ""
        expected += "\nWelcome to Zack's super-duper basic explorer."
        expected += "\nThis game allows you to visit different things."
        expected += "\nType 'help' (no quotes) to see your commands."
        self.assertEqual(Game.msg_welcome(), expected)

    def test_msg_help(self):
        expected = "Your commands are: go quit help "
        self.assertEqual(Game.msg_help(), expected)

    def test_msg_exit(self):
        expected = "Thanks for playing."
        self.assertEqual(Game.msg_exit(), expected)

    def test_gameplay_command_go(self):
        game = Game("default")  # name added for clarity
        expected = "North America"
        self.assertEqual(game.short_location(), expected)
        expected = "Going nowhere. At least we get there fast."
        self.assertEqual(game.process_command("go"), expected)
        expected = "North America"
        self.assertEqual(game.short_location(), expected)
        expected = "Nothing in that direction."
        self.assertEqual(game.process_command("go blearg"), expected)
        expected = "North America"
        self.assertEqual(game.short_location(), expected)
        expected = "Going: south"
        self.assertEqual(game.process_command("go south"), expected)
        expected = "South America"
        self.assertEqual(game.short_location(), expected)
        expected = "Going: south"
        self.assertEqual(game.process_command("go south"), expected)
        expected = "Antarctica"
        self.assertEqual(game.short_location(), expected)
        expected = "Going: northwest"
        self.assertEqual(game.process_command("go northwest"), expected)
        expected = "South America"
        self.assertEqual(game.short_location(), expected)
        expected = "Going: north"
        self.assertEqual(game.process_command("go north"), expected)
        expected = "North America"
        self.assertEqual(game.short_location(), expected)
        expected = "Going: east"
        self.assertEqual(game.process_command("go east"), expected)
        expected = "Europe"
        self.assertEqual(game.short_location(), expected)
        expected = "Going: west"
        self.assertEqual(game.process_command("go west"), expected)
        expected = "North America"
        self.assertEqual(game.short_location(), expected)

    def test_gameplay_command_help(self):
        game = Game("default")  # name added for clarity
        expected = "Your commands are: go quit help "
        self.assertEqual(game.process_command("help"), expected)

    def test_gameplay_command_empty(self):
        game = Game("default")  # name added for clarity
        expected = "Unknown command. Please try again."
        self.assertEqual(game.process_command(""), expected)

    def test_gameplay_command_bad(self):
        game = Game("default")  # name added for clarity
        expected = "Unknown command. Please try again."
        self.assertEqual(game.process_command("blearg"), expected)

    def test_gameplay_command_quit(self):
        game = Game("default")  # name added for clarity
        expected = False
        self.assertEqual(game.is_finished(), expected)
        expected = "Quitting"
        self.assertEqual(game.process_command("quit"), expected)
        expected = True
        self.assertEqual(game.is_finished(), expected)


if __name__ == '__main__':
    unittest.main()
