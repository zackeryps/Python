##
# Written By Zackery Salzwedel
# This class runs the game of zuul.
# Room building and Command logic is in this class.
# It is based on Game.java
# See project NOTES.txt for more information.
##
from CommandWord import CommandWord
from Parser import Parser
from Room import Room
from Scenarios import Scenarios


class Game:
    def __init__(self, scenario=None):
        if scenario is None:
            print(self.msg_scenario_list())
            scenario = input("Scenario: ")
        self._current_room = self.create_rooms(scenario)
        self._finished = False

    @staticmethod
    def msg_scenario_list():
        return "\nScenarios: " + Scenarios.get_scenario_list()

    @staticmethod
    def create_rooms(scenario=None):
        return Scenarios.load_scenario(scenario)

    def is_finished(self):
        return self._finished

    @staticmethod
    def msg_welcome():
        msg = "\nWelcome to Zack's super-duper basic explorer."
        msg += "\nThis game allows you to visit different things."
        msg += "\nType '" + CommandWord.HELP.value + "' (no quotes) to see your commands."
        return msg

    @staticmethod
    def msg_help():
        return "Your commands are: " + Parser.string_commands()

    def current_location(self):
        return "\nCurrent " + self._current_room.get_description_verbose()

    def short_location(self):
        return self._current_room.get_description()

    def process_command(self, inp):
        command = Parser.parse_command(inp)
        command_word = command.get_command_word()
        if command_word == CommandWord.GO:
            msg = self.go_room(command)
        elif command_word == CommandWord.HELP:
            msg = self.msg_help()
        elif command_word == CommandWord.QUIT:
            self._finished = True
            msg = "Quitting"
        elif command_word == CommandWord.UNKNOWN:
            msg = "Unknown command. Please try again."
        else:
            msg = "command processing error: unrecognized CommandWord"

        return msg

    def go_room(self, command):
        if command.has_second_word():
            direction = command.get_second_word()
            next_room = self._current_room.get_exit(direction)
            if next_room is not None:
                msg = "Going: " + direction
                self._current_room = next_room
            else:
                msg = "Nothing in that direction."
        else:
            msg = "Going nowhere. At least we get there fast."

        return msg

    @staticmethod
    def msg_exit():
        return "Thanks for playing."

##
# Original .java file had a snarky remark if there was a second word with a quit command.
# Opted to remove that
## v2:
# Original .java file output across every class.
# Attempted to move all output into strings returned by this class.
# Moved game logic flow control to driver.
##
